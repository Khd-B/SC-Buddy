# app.py
import streamlit as st

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
    },
    "Supply Chain Reliability Metrics": {
        "Supply Chain Reliability": {
            "formula": "Supply Chain Reliability = (Number of Orders Delivered On-Time and In-Full) / (Total Number of Orders)",
            "description": "Measures the percentage of orders that are delivered on-time and in-full.",
            "inputs": ["Number of Orders Delivered On-Time and In-Full", "Total Number of Orders"]
        },
        "Mean Time Between Failures (MTBF)": {
            "formula": "MTBF = Total Operating Time / Number of Failures",
            "description": "Measures the average time between equipment failures.",
            "inputs": ["Total Operating Time", "Number of Failures"]
        },
        "Mean Time To Repair (MTTR)": {
            "formula": "MTTR = Total Downtime / Number of Failures",
            "description": "Measures the average time it takes to repair equipment after a failure.",
            "inputs": ["Total Downtime", "Number of Failures"]
        }
    },
    "Supply Chain Flexibility Metrics": {
        "Supply Chain Flexibility Index": {
            "formula": "Supply Chain Flexibility Index = (Number of Supply Chain Configurations) / (Total Number of Possible Configurations)",
            "description": "Measures the ability of the supply chain to adapt to changing market conditions.",
            "inputs": ["Number of Supply Chain Configurations", "Total Number of Possible Configurations"]
        },
        "Time to Market": {
            "formula": "Time to Market = Total Time from Product Design to Launch",
            "description": "Measures the time it takes to bring a new product to market.",
            "inputs": ["Total Time from Product Design to Launch"]
        },
        "Supply Chain Responsiveness": {
            "formula": "Supply Chain Responsiveness = (Number of Orders Filled Within a Certain Timeframe) / (Total Number of Orders)",
            "description": "Measures the ability of the supply chain to respond quickly to changing customer demand.",
            "inputs": ["Number of Orders Filled Within a Certain Timeframe", "Total Number of Orders"]
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
    elif metric_name == "Supply Chain Reliability":
        return inputs["Number of Orders Delivered On-Time and In-Full"] / inputs["Total Number of Orders"]
    elif metric_name == "Mean Time Between Failures (MTBF)":
        return inputs["Total Operating Time"] / inputs["Number of Failures"]
    elif metric_name == "Mean Time To Repair (MTTR)":
        return inputs["Total Downtime"] / inputs["Number of Failures"]
    elif metric_name == "Supply Chain Flexibility Index":
        return inputs["Number of Supply Chain Configurations"] / inputs["Total Number of Possible Configurations"]
    elif metric_name == "Time to Market":
        return inputs["Total Time from Product Design to Launch"]
    elif metric_name == "Supply Chain Responsiveness":
        return inputs["Number of Orders Filled Within a Certain Timeframe"] / inputs["Total Number of Orders"]
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
        for metric in category_metrics:
            if st.sidebar.checkbox(metric):
                selected_metrics.append(metric)

    # Debugging: Print selected metrics
    st.sidebar.write("Selected Metrics:", selected_metrics)

    # Display input fields and calculate results
    for metric in selected_metrics:
        st.markdown(f"### {metric}")
        st.write(f"**Formula:** {metrics[metric]['formula']}")
        st.write(f"**Description:** {metrics[metric]['description']}")

        inputs = {}
        for input_field in metrics[metric]['inputs']:
            inputs[input_field] = st.number_input(input_field, value=0.0, key=f"{metric}_{input_field}")

        if st.button(f"Calculate {metric}", key=f"calculate_{metric}"):
            result = calculate_metric(metric, inputs)
            st.success(f"**Result:** {result}")

    # Reset button
    if st.button("Reset"):
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    main()
