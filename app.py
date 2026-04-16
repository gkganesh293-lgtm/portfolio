import streamlit as st

st.set_page_config(page_title="Shashank Portfolio", layout="wide")

# Sidebar
st.sidebar.title("👨‍💻 Shashank")
st.sidebar.write("Aspiring Data Analyst")
st.sidebar.write("📧 gkganesh293@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/shashank-khadka-169539147/)")
st.sidebar.write("[GitHub](https://github.com/gkganesh293-lgtm)")

# Main
st.title("👋 Hi, I'm Shashank")
st.subheader("Data Analyst | Power BI | Excel | Python")

st.write("""
I solve real-world problems using data.
""")

# Skills
st.header("🛠 Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Excel")
    st.write("SQL")

with col2:
    st.write("Power BI")
    st.write("Dashboard")

with col3:
    st.write("Python")
    st.write("Pandas")

# Projects
st.header("📊 Projects")

st.subheader("♻️ Solid Waste Management")
st.write("Optimized waste collection using data analysis.")

st.subheader("📈 Sales Dashboard")
st.write("Created dashboard to track revenue and profit.")

# Contact
st.header("📞 Contact")
st.write("Email: yourmail@gmail.com")