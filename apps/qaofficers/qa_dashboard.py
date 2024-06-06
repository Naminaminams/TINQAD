import dash_bootstrap_components as dbc
from dash import dash, html, dcc, Input, Output, State

from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime 

from apps import commonmodules as cm
from app import app
from apps import dbconnect as db




# Get the current year
current_year = datetime.now().year

# Function to fetch the total count of Arts and Letters QA Officers
@app.callback(
    Output('get_total_asl', 'children'),
    [Input('url', 'pathname')]
)
def get_total_asl(pathname):
    total_count = None
    if pathname == '/QAOfficers_dashboard': 
        sql = """
            SELECT COUNT(*) 
            FROM qaofficers.qa_officer 
            WHERE 
                qaofficer_cluster_id = 1
                AND qaofficer_del_ind IS False
        """ 
        total_count = db.query_single_value(sql)
    return total_count


# Function to fetch the total count of Management and Economics QA Officers
@app.callback(
    Output('get_total_mae', 'children'),
    [Input('url', 'pathname')]
)
def get_total_mae(pathname):
    total_count = None
    if pathname == '/QAOfficers_dashboard': 
        sql = """
            SELECT COUNT(*) 
            FROM qaofficers.qa_officer 
            WHERE 
                qaofficer_cluster_id = 2
                AND qaofficer_del_ind IS False
        """ 
        total_count = db.query_single_value(sql)
    return total_count
 


# Function to fetch the total count of Scienece and Technology QA Officers
@app.callback(
    Output('get_total_sat', 'children'),
    [Input('url', 'pathname')]
)
def get_total_sat(pathname):
    total_count = None
    if pathname == '/QAOfficers_dashboard': 
        sql = """
            SELECT COUNT(*) 
            FROM qaofficers.qa_officer 
            WHERE 
                qaofficer_cluster_id = 3
                AND qaofficer_del_ind IS False
        """ 
        total_count = db.query_single_value(sql)
    return total_count
 
 
# Function to fetch the total count of Social Scieneces and Law Qa Officers
@app.callback(
    Output('get_total_ssl', 'children'),
    [Input('url', 'pathname')]
)
def get_total_ssl(pathname):
    total_count = None
    if pathname == '/QAOfficers_dashboard': 
        sql = """
            SELECT COUNT(*) 
            FROM qaofficers.qa_officer 
            WHERE 
                qaofficer_cluster_id = 4
                AND qaofficer_del_ind IS False
        """ 
        total_count = db.query_single_value(sql)
    return total_count
 

facultytrainedcard = dbc.Card(
    [
        dbc.CardHeader(html.H5(html.B("No. of faculty with QA Training"))), 
        dbc.CardBody(
            [ 
                dbc.Row(
                    [
                        
                        dbc.Col(
                            html.Span(id='get_total_asl', style={"font-weight": "bold"}), 
                            style={
                                "backgroundColor": "#f8d7da",
                                'height': '70px', 
                                'width': '70px',
                                "borderRadius": "10px",
                                "padding": "10px",
                                'margin': 'auto', 
                                "textAlign": "center",
                                "marginLeft": "-10px" 
                            }
                        ),   
                        dbc.Col(
                            html.Span(id='get_total_mae', style={"font-weight": "bold"}), 
                            style={
                                "backgroundColor": "#cce5ff",
                                'height': '70px', 
                                'width': '70px',
                                "borderRadius": "10px",
                                "padding": "10px",
                                'margin': 'auto', 
                                "textAlign": "center",
                                "marginLeft": "-10px" 
                            }
                        ),   
                        dbc.Col(
                            html.Span(id='get_total_sat', style={"font-weight": "bold"}), 
                            style={
                                "backgroundColor": "#d4edda",
                                'height': '70px', 
                                'width': '70px',
                                "borderRadius": "10px",
                                "padding": "10px",
                                'margin': 'auto', 
                                "textAlign": "center",
                                "marginLeft": "-10px" 
                            }
                        ),   
                        dbc.Col(
                            html.Span(id='get_total_ssl', style={"font-weight": "bold"}), 
                            style={
                                "backgroundColor": "#fff3cd",
                                'height': '70px', 
                                'width': '70px',
                                "borderRadius": "10px",
                                "padding": "10px",
                                'margin': 'auto', 
                                "textAlign": "center",
                                "marginLeft": "-10px" 
                            }
                        ),    
                         
                    ]
                ),
                dbc.Row(
                    [ 
                        dbc.Col(
                            html.Strong("Arts and Letters", style={'textAlign': 'center'}),
                            width="auto"
                        ),
                        dbc.Col(
                            html.Strong("Management and Economics", style={'textAlign': 'center'}),
                            width="auto"
                        ),
                        dbc.Col(
                            html.Strong("Science and Technology", style={'textAlign': 'center'}),
                            width="auto"
                        ),
                        dbc.Col(
                            html.Strong("Social Sciences and Law", style={'textAlign': 'center'}),
                            width="auto"
                        ),

                    ]
                ),
            ]   
        ),   
    ],
    className="mb-3", 
    style={'margin': '10 10px'} 
)



trainedofficerscard = dbc.Card(
    dbc.CardBody([
        dbc.Row(
            [
                dbc.Col(  
                    html.H5(html.B("Total Trained Officers")),  
                    
                ), 
                dbc.Col(
                    dcc.Input(
                        id='qatr_currentyear',
                        type='number',   
                        value=current_year, 
                        style={'width': '100%'}, 
                    ),
                    width=2,  
                ),
            ],
            className="my-2"  
        ),
        dbc.Row(
            [
                dbc.Col( 
                    html.Div(
                        id='trainedofficers_clusterlist', 
                            style={
                                'marginTop': '20px',
                                'overflowX': 'auto'  # This CSS property adds a horizontal scrollbar
                                }
                        ),
                    )
                ]
            )
        ]
    ),
    className="mb-3",  
)





layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    cm.generate_navbar(),
                    width=2
                ),
                dbc.Col(
                    [
                        html.H1("QA OFFICERS DASHBOARD"),
                        html.Hr(),
                        html.Br(),

                        facultytrainedcard,
                        trainedofficerscard,

                        dbc.Row(   
                            [
                                dbc.Col(  
                                    dbc.Input(
                                        type='text',
                                        id='qaotraininglist_filter',
                                        placeholder='🔎 Search by name, email, position, etc',
                                        className='ml-auto'   
                                    ),
                                    width="8",
                                ),
                                dbc.Col(   
                                    dbc.Button(
                                        "➕ Add Training", color="primary", 
                                        href='/QAOfficers/addtraining', 
                                    ),
                                    width="auto", 
                                    className="ml-auto",   
                                ),
                                dbc.Col(   
                                    dbc.Button(
                                        "View Data List", color="warning", 
                                        href='/QAOfficers/datalist', 
                                    ),
                                    width="auto",    
                                ),
                            ],
                            className="align-items-center",   
                            style={
                                "margin-right": "2px",
                                "margin-bottom": "15px",
                            }
                        ), 

                        

                        html.Div(
                            id='qaotraininglist_list', 
                            style={
                            'overflowX': 'auto', 
                            'overflowY': 'auto',   
                            'maxHeight': '200px',
                            }
                        ),

                        html.Br(),
                        html.Br(),
                        
                    ], 
                    width=9, style={'marginLeft': '15px'}
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row (
            [
                dbc.Col(
                    cm.generate_footer(), width={"size": 12, "offset": 0}
                ),
            ]
        )
    ]
)








@app.callback(
    [Output('trainedofficers_clusterlist', 'children')],
    [
        Input('url', 'pathname'),
        Input('qatr_currentyear', 'value')
    ]
    )

def clustertraininglist_loadlist(pathname, search_term):
    if pathname == '/QAOfficers_dashboard': 
        # SQL query to create a pivot table with specific training types as columns
        sql = """
            SELECT 
                clus.cluster_name AS "Academic Cluster",
                qtd.qatr_training_year AS "Year",
                COUNT(CASE WHEN tt.trainingtype_name = 'AUN-QA Tier 1' THEN 1 ELSE NULL END) AS "Tier 1",
                COUNT(CASE WHEN tt.trainingtype_name = 'AUN-QA Tier 2' THEN 1 ELSE NULL END) AS "Tier 2",
                COUNT(CASE WHEN tt.trainingtype_name = 'AUN-QA Tier 3' THEN 1 ELSE NULL END) AS "Tier 3",
                COUNT(CASE WHEN tt.trainingtype_name = 'AUN-QA SAR Writing Workshop' THEN 1 ELSE NULL END) AS "SAR Writing Workshop",
                COUNT(CASE WHEN tt.trainingtype_name = 'UP System External Reviewers Training' THEN 1 ELSE NULL END) AS "External Reviewers",
                COUNT(CASE WHEN tt.trainingtype_name = 'Others' THEN 1 ELSE NULL END) AS "Others"
            FROM 
                qaofficers.qa_training_details AS qtd
            LEFT JOIN 
                qaofficers.qa_officer AS qo
                ON qtd.qatr_officername_id = qo.qaofficer_id
            LEFT JOIN 
                public.clusters AS clus
                ON qo.qaofficer_cluster_id = clus.cluster_id
            LEFT JOIN
                qaofficers.training_type AS tt
                ON qtd.qatr_training_type = tt.trainingtype_id
            WHERE 
                qatr_training_del_ind IS False
            GROUP BY 
                clus.cluster_name, qtd.qatr_training_year
            ORDER BY 
                clus.cluster_name, qtd.qatr_training_year
        """
        
        # Define the expected columns for the table
        cols = ['Academic Cluster', 'Year', 'Tier 1', 'Tier 2', 'Tier 3', 'SAR Writing Workshop', 'External Reviewers', 'Others']

        # Query data from the database
        df = db.querydatafromdatabase(sql, [], cols)

        # Apply search term filter
        if search_term is not None:
            df = df[df['Year'] == search_term]  # Filter by the search term (year)

        # Generate the table from the DataFrame
        if not df.empty:
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, size='sm')
            return [table]
        else:
            return [html.Div("No records to display")]
    else:
        raise PreventUpdate


@app.callback(
    [
        Output('qaotraininglist_list', 'children')
    ],
    [
        Input('url', 'pathname'),
        Input('qaotraininglist_filter', 'value'),
    ]
    )

def traininglist_loadlist(pathname, searchterm):
    if pathname == '/QAOfficers_dashboard': 
        sql = """
            SELECT 
                qo.qaofficer_full_name AS "Name",
                cp.cuposition_name AS "Rank/Designation",
                du.deg_unit_name AS "Department",
                cl.college_name AS "College",
                clus.cluster_name AS "Academic Cluster",
                STRING_AGG(qtd.qatr_training_name, ', ') AS "Trainings"
            FROM 
                qaofficers.qa_officer AS qo
            LEFT JOIN 
                qaofficers.qa_training_details AS qtd
                ON qo.qaofficer_id = qtd.qatr_officername_id
            LEFT JOIN 
                qaofficers.cuposition AS cp
                ON qo.qaofficer_cuposition_id = cp.cuposition_id
            LEFT JOIN 
                public.deg_unit AS du
                ON qo.qaofficer_deg_unit_id = du.deg_unit_id
            LEFT JOIN 
                public.college AS cl
                ON qo.qaofficer_college_id = cl.college_id
            LEFT JOIN 
                public.clusters AS clus
                ON qo.qaofficer_cluster_id = clus.cluster_id
            WHERE
                qo.qaofficer_del_ind IS False
            
            GROUP BY 
                qo.qaofficer_full_name, cp.cuposition_name, du.deg_unit_name, cl.college_name, clus.cluster_name
        
        """
        cols = ['Name', 'Rank/Designation', 'Department','College','Academic Cluster', 'Trainings']   

        if searchterm:
            sql += """
                WHERE
                    qaofficer_sname ILIKE %s OR
                    qaofficer_fname ILIKE %s OR
                    qaofficer_role ILIKE %s
            """
            like_pattern = f"%{searchterm}%"
            values = [like_pattern] * 3
        else:
            values = []

        df = db.querydatafromdatabase(sql, values, cols) 

        # Generate the table from the DataFrame
        if not df.empty:
            table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, size='sm')
            return [table]
        else:
            return [html.Div("No records yet.")]
    else:
        raise PreventUpdate