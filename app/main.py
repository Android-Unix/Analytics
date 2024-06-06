import streamlit as st # type: ignore

from performance_statistics import PerformanceStatistics


def main():
    st.write("This is a sample Streamlit app running in Docker.")
    performance_statistics = PerformanceStatistics()
    performance_statistics.get_player_performance_report()
    performance_statistics.get_team_performance_report()

if __name__ == "__main__":
    main()
