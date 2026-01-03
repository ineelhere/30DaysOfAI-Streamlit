import streamlit as st
import importlib.util
import sys
from pathlib import Path

st.set_page_config(page_title="30 Days of AI", layout="wide")

# Sidebar Header
st.sidebar.title("🤖 30 Days of AI Challenge")

# Get all available day folders
base_path = Path(__file__).parent
day_folders = sorted([d for d in base_path.iterdir() if d.is_dir() and d.name.startswith("day")])

if not day_folders:
    st.warning("No day folders found. Please create day1/, day2/, etc. folders with their respective Python files.")
else:
    # Create dropdown in sidebar
    day_options = [d.name.replace("day", "Day ") for d in day_folders]
    selected_day = st.sidebar.selectbox("📅 Select a Day:", day_options)
    
    # Get the selected day folder and file
    selected_idx = day_options.index(selected_day)
    selected_folder = day_folders[selected_idx]
    day_file = selected_folder / f"{selected_folder.name}.py"
    
    # Check if the day file exists
    if day_file.exists():
        st.divider()
        
        # Load and execute the day file
        try:
            spec = importlib.util.spec_from_file_location(selected_folder.name, day_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[selected_folder.name] = module
            spec.loader.exec_module(module)
        except Exception as e:
            st.error(f"Error loading {selected_folder.name}: {str(e)}")
    else:
        st.error(f"File not found: {day_file}")
