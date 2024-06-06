import streamlit as st # type: ignore
import pandas as pd # type: ignore
import os
import numpy # type: ignore


class PerformanceStatistics:
    """
        class to get performance statistics
    """

    def get_player_performance_report(self):
        """
            get player performance report        
        """

        resources_path = 'resources/player'
        resources = self._get_resources(resources_path)

        d_types = self._get_dtypes(f'{resources_path}/{resources[0]}')
        df_player_home = pd.read_csv(f'{resources_path}/{resources[0]}', index_col='Player', dtype=d_types)
        df_player_home.reset_index(inplace=True)

        d_types = self._get_dtypes(f'{resources_path}/{resources[1]}')
        df_player_away = pd.read_csv(f'{resources_path}/{resources[1]}', index_col='Player', dtype=d_types)
        df_player_away.reset_index(inplace=True)

        st.write("Player Home")
        st.line_chart(df_player_home, x='Player', use_container_width=True, y='PTS')

        st.write("Player Away")
        st.line_chart(df_player_away, x='Player', use_container_width=True, y='PTS')

        avg_points = self._get_mean(df_player_home, df_player_away, 'PTS')
        st.write(f"Average Points: {avg_points}")

        avg_assists = self._get_mean(df_player_home, df_player_away, 'AST')
        st.write(f"Average Assists: {avg_assists}")
        
        avg_rebounds = self._get_mean(df_player_home, df_player_away, 'REB')
        st.write(f"Average Rebounds: {avg_rebounds}")

        avg_steals = self._get_mean(df_player_home, df_player_away, 'STL')
        st.write(f"Average Steals: {avg_steals}")

        avg_blocks = self._get_mean(df_player_home, df_player_away, 'BLK')
        st.write(f"Average Blocks: {avg_blocks}")

        avg_metrics = pd.DataFrame(
            {
                'player': df_player_home['Player'],
                'points': (df_player_home['PTS'] + df_player_away['PTS']) / 2,
                'assists': (df_player_home['AST'] + df_player_away['AST']) / 2,
                'rebounds': (df_player_home['REB'] + df_player_away['REB']) / 2,
                'steals': (df_player_home['STL'] + df_player_away['STL']) / 2,
                'blocks': (df_player_home['BLK'] + df_player_away['BLK']) / 2,
            }
        )
        st.write("Average Metrics")
        st.bar_chart(avg_metrics, use_container_width=True, x='player', y='points')
        st.bar_chart(avg_metrics, use_container_width=True, x='player', y='assists')
        st.bar_chart(avg_metrics, use_container_width=True, x='player', y='rebounds')
        st.bar_chart(avg_metrics, use_container_width=True, x='player', y='steals')
        st.bar_chart(avg_metrics, use_container_width=True, x='player', y='blocks')


        st.write("Player Performance Metrics (Home vs Away)")

        metrics = pd.DataFrame(
            {
                'player': df_player_home['Player'],
                'points': df_player_home['PTS'] - df_player_away['PTS'],
                'assists': df_player_home['AST'] - df_player_away['AST'],
                'rebounds': df_player_home['REB'] - df_player_away['REB'],
                'steals': df_player_home['STL'] - df_player_away['STL'],
                'blocks': df_player_home['BLK'] - df_player_away['BLK'],
            }
        )

        st.bar_chart(metrics, use_container_width=True, x='player', y='points')
        st.line_chart(metrics, use_container_width=True, x='player', y='assists')
        st.line_chart(metrics, use_container_width=True, x='player', y='rebounds')
        st.line_chart(metrics, use_container_width=True, x='player', y='steals')
        st.line_chart(metrics, use_container_width=True, x='player', y='blocks')


    def get_team_performance_report(self):
        """
            get team performance report
        """

        resources_path = 'resources/team'
        resources = self._get_resources(resources_path)

        d_types = self._get_dtypes(f'{resources_path}/{resources[0]}')
        df_team_home = pd.read_csv(f'{resources_path}/{resources[0]}', index_col='Team', dtype=d_types)
        df_team_home.reset_index(inplace=True)

        d_types = self._get_dtypes(f'{resources_path}/{resources[1]}')
        df_team_away = pd.read_csv(f'{resources_path}/{resources[1]}', index_col='Team', dtype=d_types)
        df_team_away.reset_index(inplace=True)

        st.write("Team Home")
        st.line_chart(df_team_home, use_container_width=True, y='PTS')

        st.write("Team Away")
        st.line_chart(df_team_away, use_container_width=True, y='PTS')

        avg_points = self._get_mean(df_team_home, df_team_away, 'PTS')
        st.write(f"Average Points: {avg_points}")

        avg_assists = self._get_mean(df_team_home, df_team_away, 'AST')
        st.write(f"Average Assists: {avg_assists}")
        
        avg_rebounds = self._get_mean(df_team_home, df_team_away, 'REB')
        st.write(f"Average Rebounds: {avg_rebounds}")

        avg_steals = self._get_mean(df_team_home, df_team_away, 'STL')
        st.write(f"Average Steals: {avg_steals}")

        avg_blocks = self._get_mean(df_team_home, df_team_away, 'BLK')
        st.write(f"Average Blocks: {avg_blocks}")

        avg_metrics = pd.DataFrame(
            {
                'team': df_team_home['Team'],
                'points': (df_team_home['PTS'] + df_team_away['PTS']) / 2,
                'assists': (df_team_home['AST'] + df_team_away['AST']) / 2,
                'rebounds': (df_team_home['REB'] + df_team_away['REB']) / 2,
                'steals': (df_team_home['STL'] + df_team_away['STL']) / 2,
                'blocks': (df_team_home['BLK'] + df_team_away['BLK']) / 2,
            }
        )
        st.write("Average Metrics")
        st.bar_chart(avg_metrics, use_container_width=True, x='team', y='points')
        st.bar_chart(avg_metrics, use_container_width=True, x='team', y='assists')
        st.bar_chart(avg_metrics, use_container_width=True, x='team', y='rebounds')
        st.bar_chart(avg_metrics, use_container_width=True, x='team', y='steals')
        st.bar_chart(avg_metrics, use_container_width=True, x='team', y='blocks')

        st.write("Team Performance Metrics (Home vs Away)")

        metrics = pd.DataFrame(
            {
                'team': df_team_home['Team'],
                'points': df_team_home['PTS'] - df_team_away['PTS'],
                'assists': df_team_home['AST'] - df_team_away['AST'],
                'rebounds': df_team_home['REB'] - df_team_away['REB'],
                'steals': df_team_home['STL'] - df_team_away['STL'],
                'blocks': df_team_home['BLK'] - df_team_away['BLK'],
            }
        )

        st.bar_chart(metrics, use_container_width=True, x='team', y='points')
        st.line_chart(metrics, use_container_width=True, x='team', y='assists')
        st.line_chart(metrics, use_container_width=True, x='team', y='rebounds')
        st.line_chart(metrics, use_container_width=True, x='team', y='steals')
        st.line_chart(metrics, use_container_width=True, x='team', y='blocks')


    def _get_resources_paths(self, prefix: str = 'resources'):
        # get the path of the file
        # get root folder and resource folder

        root_folder = os.path.dirname(os.path.abspath(__file__))
        resources_path = root_folder + '/' + prefix
        return resources_path


    def _get_resources(self, resources_path: str):
        resources = []

        for file in os.listdir(resources_path):
            if file.endswith('.csv'):
                resources.append(file)

        return resources


    def _get_dtypes(self, file_path: str):
        # get the data types of the file
        # return the data types

        headers = self._get_headers(file_path)
        d_types = self._get_dtypes_mapping()
        return {header: d_types[header] for header in headers}


    def _get_headers(self, file_path: str):
        # get the headers of the file
        # return the headers

        df = pd.read_csv(file_path, nrows=1)
        return df.columns.tolist()


    def _get_dtypes_mapping(self):
        # get the data types mapping
        # return the data types mapping

        return {
            'Player': 'str',
            'Team': 'str',
            'Age': numpy.int64,
            'GP': numpy.int64,
            'W': numpy.int64,
            'L': numpy.int64,
            'Min': numpy.float64,
            'PTS': numpy.float64,
            'FGM': numpy.float64,
            'FGA': numpy.float64,
            'FG%': numpy.float64,
            '3PM': numpy.float64,
            '3PA': numpy.float64,
            '3P%': numpy.float64,
            'FTM': numpy.float64,
            'FTA': numpy.float64,
            'FT%': numpy.float64,
            'OREB': numpy.float64,
            'DREB': numpy.float64,
            'REB': numpy.float64,
            'AST': numpy.float64,
            'TOV': numpy.float64,
            'STL': numpy.float64,
            'BLK': numpy.float64,
            'BLKA': numpy.float64,
            'PF': numpy.float64,
            'PFD': numpy.float64,
            'FP': numpy.float64,
            'DD2': numpy.int64,
            'TD3': numpy.int64,
            '+/-': numpy.float64,
            'WIN%': numpy.float64,
        }


    def _get_mean(self, df_home: pd.DataFrame, df_away: pd.DataFrame, column: str) -> object:
        # get the mean of the dataframe
        # return the mean

        home_points_mean = df_home.loc[:, column].mean()
        away_points_mean = df_away.loc[:, column].mean()

        return (home_points_mean + away_points_mean) / 2
