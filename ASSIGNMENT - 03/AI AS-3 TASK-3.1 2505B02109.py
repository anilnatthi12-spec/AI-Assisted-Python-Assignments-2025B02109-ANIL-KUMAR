import sys
from typing import Tuple, Dict
TARIFFS = {
    "DOMESTIC": {
        "fixed_charge_per_kw": 10.00,  # Rs. 10/kW/month (LT-I Domestic)
        "min_fixed_charge": 50.00,     # Minimum fixed charge per month
        "customer_charge": 30.00,      # Fixed customer charge (CC)
        "ed_rate": 0.06,               # Electricity Duty (ED) assumed at 6% of EC
        "slabs": [
            (200, 5.10),   # 0 - 200 units @ Rs. 5.10/unit
            (100, 7.70),   # 201 - 300 units @ Rs. 7.70/unit (i.e., next 100)
            (100, 9.00),   # 301 - 400 units @ Rs. 9.00/unit (i.e., next 100)
            (400, 9.50),   # 401 - 800 units @ Rs. 9.50/unit (i.e., next 400)
            (float('inf'), 10.00) # Above 800 units @ Rs. 10.00/unit
        ]
    },
    "COMMERCIAL": {
        "fixed_charge_per_kw": 70.00,  # Rs. 70/kW/month (LT-II Non-Domestic)
        "min_fixed_charge": 100.00,    # Minimum fixed charge per month
        "customer_charge": 50.00,      # Fixed customer charge (CC)
        "ed_rate": 0.06,               # Electricity Duty (ED) assumed at 6% of EC
        "slabs": [
            (100, 8.50),    # 0 - 100 units @ Rs. 8.50/unit
            (200, 9.90),    # 101 - 300 units @ Rs. 9.90/unit (i.e., next 200)
            (200, 10.40),   # 301 - 500 units @ Rs. 10.40/unit (i.e., next 200)
            (float('inf'), 11.00) # Above 500 units @ Rs. 11.00/unit
        ]
    }
}

def calculate_energy_charges(units_consumed: float, slabs: list) -> float:
    remaining_units = units_consumed
    energy_charge = 0.0

    for slab_limit, rate in slabs:
        if remaining_units <= 0:
            break
        units_in_slab = min(remaining_units, slab_limit)

        charge_for_slab = units_in_slab * rate
        energy_charge += charge_for_slab
        remaining_units -= units_in_slab

    return round(energy_charge, 2)

def generate_bill(
    previous_units: float,
    current_units: float,
    customer_type: str,
    connected_load_kW: float
) -> Tuple[Dict[str, float], float]:
    if current_units < previous_units:
        raise ValueError("Current units (CU) must be greater than or equal to Previous units (PU).")

    units_consumed = current_units - previous_units
    if customer_type.upper() == 'D':
        tariff_key = "DOMESTIC"
    elif customer_type.upper() == 'C':
        tariff_key = "COMMERCIAL"
    else:
        raise ValueError("Invalid customer type. Use 'D' for Domestic or 'C' for Commercial.")
    tariff = TARIFFS[tariff_key]
    energy_charges = calculate_energy_charges(units_consumed, tariff["slabs"])
    fixed_charge_calculated = connected_load_kW * tariff["fixed_charge_per_kw"]
    fixed_charge = max(fixed_charge_calculated, tariff["min_fixed_charge"])

    customer_charge = tariff["customer_charge"]
    electricity_duty = round(energy_charges * tariff["ed_rate"], 2)
    total_bill = fixed_charge + customer_charge + energy_charges + electricity_duty
    charge_components = {
        "PU_Reading": previous_units,
        "CU_Reading": current_units,
        "Units_Consumed": units_consumed,
        "Connected_Load_kW": connected_load_kW,
        "EC_Energy_Charges": energy_charges,
        "FC_Fixed_Charges": fixed_charge,
        "CC_Customer_Charges": customer_charge,
        "ED_Electricity_Duty": electricity_duty,
        "Total_Bill_Amount": round(total_bill, 2)
    }
    return charge_components, round(total_bill, 2)
def main():
    """Main function to handle user input and display the calculated bill."""
    print("--- TGNPDCL Electricity Bill Calculator ---")
    try:
        previous_units = float(input("Enter Previous Unit Reading (PU): "))
        current_units = float(input("Enter Current Unit Reading (CU): "))
        customer_type_input = input("Enter Customer Type ('D' for Domestic, 'C' for Commercial): ").strip().upper()
        connected_load_kW = float(input("Enter Connected Load in kW (e.g., 2.0): "))
        customer_name = input("Enter Customer Name: ").strip()
        mobile_number = input("Enter Mobile Number: ").strip()
        components, total_bill = generate_bill(
            previous_units,
            current_units,
            customer_type_input,
            connected_load_kW
        )

        units_consumed = components["Units_Consumed"]
        print("\n--- Bill Summary ---")
        print(f"Customer Name: {customer_name}")
        print(f"Mobile Number: {mobile_number}")
        print(f"Customer Type: {'Domestic' if customer_type_input == 'D' else 'Commercial'} (LT-{1 if customer_type_input == 'D' else 2})")
        print(f"Connected Load: {connected_load_kW:.2f} kW")
        print(f"Units Consumed: {units_consumed:.2f} kWh")
        print("-" * 30)

        print(f"EC (Energy Charges): {components['EC_Energy_Charges']:>15.2f} Rs.")
        print(f"FC (Fixed Charges): {components['FC_Fixed_Charges']:>16.2f} Rs.")
        print(f"CC (Customer Charges): {components['CC_Customer_Charges']:>14.2f} Rs.")
        print(f"ED (Electricity Duty): {components['ED_Electricity_Duty']:>14.2f} Rs.")
        print("-" * 30)
        print(f"Total Bill Amount: {components['Total_Bill_Amount']:>13.2f} Rs.")
        print("---------------------------------")

    except ValueError as e:
        print(f"\nError: Invalid input. {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
