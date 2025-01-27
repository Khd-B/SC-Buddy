# import streamlit as st

# Define formulas and descriptions for each metric
metrics = {
    "Inventory Metrics": {
        "Inventory Turnover": {
            "formula": "Inventory Turnover = Cost of Goods Sold (COGS) / Average Inventory",
            "description": "Measures how quickly inventory is sold and replaced.",
            "inputs": ["Cost of Goods Sold (COGS)", "Average Inventory"]
        },
        "Inventory Days of Supply": {
            "formula": "Inventory Days of Supply = Average Inventory / Average Daily Demand",
            "description": "Measures the number of days inventory will last at current demand levels.",
            "inputs": ["Average Inventory", "Average Daily Demand"]
        },
        "Fill Rate": {
            "formula": "Fill Rate = (Number of Orders Filled Completely) / (Total Number of Orders)",
            "description": "Measures the percentage of customer orders that are filled completely from existing inventory.",
            "inputs": ["Number of Orders Filled Completely", "Total Number of Orders"]
        }
    },
    "Logistics and Transportation Metrics": {
        "On-Time Delivery Rate": {
            "formula": "On-Time Delivery Rate = (Number of Deliveries Made On-Time) / (Total Number of Deliveries)",
            "description": "Measures the percentage of deliveries made on or before the scheduled delivery date.",
            "inputs": ["Number of Deliveries Made On-Time", "Total Number of Deliveries"]
        },
        "Transportation Cost as a Percentage of Revenue": {
            "formula": "Transportation Cost as a Percentage of Revenue = (Transportation Cost) / (Revenue)",
            "description": "Measures the cost of transportation as a percentage of total revenue.",
            "inputs": ["Transportation Cost", "Revenue"]
        },
        "Freight Cost Per Unit": {
            "formula": "Freight Cost Per Unit = Total Freight Cost / Total Number of Units Shipped",
            "description": "Measures the average cost of shipping one unit of product.",
            "inputs": ["Total Freight Cost", "Total Number of Units Shipped"]
        }
    }
}

# Function to calculate metrics
def calculate_metric(metric_name, inputs):
    if metric_name == "Inventory Turnover":
        return inputs["Cost of Goods Sold (COGS)"] / inputs["Average Inventory"]
    elif metric_name == "Inventory Days of Supply":
        return inputs["Average Inventory"] / inputs["Average Daily Demand"]
    elif metric_name == "Fill Rate":
        return inputs["Number of Orders Filled Completely"] / inputs["Total Number of Orders"]
    elif metric_name == "On-Time Delivery Rate":
        return inputs["Number of Deliveries Made On-Time"] / inputs["Total Number of Deliveries"]
    elif metric_name == "Transportation Cost as a Percentage of Revenue":
        return inputs["Transportation Cost"] / inputs["Revenue"]
    elif metric_name == "Freight Cost Per Unit":
        return inputs["Total Freight Cost"] / inputs["Total Number of Units Shipped"]
    else:
        return None

# Streamlit App
def main():
    st.title("SC Buddy - Supply Chain Calculator")
    st.sidebar.header("Select Metrics")

    # Checkbox for selecting metrics
    selected_metrics = []
    for category, category_metrics in metrics.items():
        st.sidebar.markdown(f"**{category}**")
        for metric_name, metric_details in category_metrics.items():
            if st.sidebar.checkbox(metric_name):
                selected_metrics.append((metric_name, metric_details))  # Append as a tuple

    # Display input fields and calculate results
    for metric_name, details in selected_metrics:
        st.markdown(f"### {metric_name}")
        st.write(f"**Formula:** {details['formula']}")
        st.write(f"**Description:** {details['description']}")

        inputs = {}
        for input_field in details["inputs"]:
            inputs[input_field] = st.number_input(input_field, value=0.0, key=f"{metric_name}_{input_field}")

        if st.button(f"Calculate {metric_name}", key=f"calculate_{metric_name}"):
            result = calculate_metric(metric_name, inputs)
            if result is not None:
                st.success(f"**Result:** {result}")
            else:
                st.warning("Unable to calculate the metric. Please check your inputs.")

    # Reset button
    if st.button("Reset"):
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    main()
