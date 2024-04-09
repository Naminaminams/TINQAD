import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dash_table
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from apps import commonmodules as cm
from app import app
from apps import dbconnect as db

import bcrypt
import base64
import hashlib

def hash_password(password):
    # Convert the password to bytes if it's a string
    password_bytes = password.encode('utf-8')

    # Generate a salt
    salt = bcrypt.gensalt()

    # Generate the hashed password
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password

form = dbc.Form(
    [
        dbc.Row(
            [
                dbc.Label("First Name", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_fname'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("Middle Name", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_mname'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        # Surname
        dbc.Row(
            [
                dbc.Label("Surname", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_sname'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        # Lived Name
        dbc.Row(
            [
                dbc.Label("Lived Name", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_livedname'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("Sex Assigned at Birth", width=4),
                dbc.Col(
                    dbc.Select(
                        id='user_sex',
                        options=[ 
                            {'label': 'Female', 'value': '2'},
                            {'label': 'Male', 'value': '1'}, 
                        ]
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("Birthday", width=4),
                dbc.Col(
                    dbc.Input(type="date", id='user_bday'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("Phone Number", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_phone_num'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("ID Number", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_id_num'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label("Office", width=4),
                dbc.Col(
                    dbc.Select(
                        id='user_office',
                        options=[ 
                            {'label': "Quality Assurance Office", 'value': '1'},
                            {'label': "Office of the Vice President for Academic Affairs", 'value': '2'},
                            {'label': "Office of the Chancellor", 'value': '3'},
                            {'label': "Office of the Vice Chancellor for Academic Affairs", 'value': '4'},
                            {'label': "Office of the Vice Chancellor for Research and Development", 'value': '5'},
                            {'label': "Office of the Vice Chancellor for Administration", 'value': '6'},
                            {'label': "Office of the Vice Chancellor for Student Affairs", 'value': '7'},
                            {'label': "Office of the Vice Chancellor for Community Affairs", 'value': '8'},
                            {'label': "Office of the Vice Chancellor for Planning and Development", 'value': '9'},
                            {'label': "UP Diliman Information Office (UPDIO)", 'value': '10'}
                        ]
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        dbc.Row(
            [
                dbc.Label("Position", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_position'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        dbc.Row(
            [
                dbc.Label("Email Address", width=4),
                dbc.Col(
                    dbc.Input(type="text", id='user_email'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        dbc.Row(
            [
                dbc.Label("Password", width=4),
                dbc.Col(
                    dbc.Input(type="password", id='user_password'),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
 
        dbc.Row(
            [
                dbc.Label("Confirm Password", width=4),
                dbc.Col(
                    dbc.Input(type="password", id = 'confirm_password', placeholder = 'Confirm password' ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        # Access Type
        dbc.Row(
            [
                dbc.Label("Access Type", width=4),
                dbc.Col(
                    dbc.Select(
                        id='user_access_type',
                        options=[ 
                            {'label': 'Basic Access', 'value': '1'},
                            {'label': 'Full Access', 'value': '2'}, 
                        ]
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),

        
        
 
 
 
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button("Save", color="primary", className="me-3", id="save_button", n_clicks=0),
                    width="auto"
                ),
                dbc.Col(
                    dbc.Button("Cancel", color="secondary", id="cancel_button", n_clicks=0),
                    width="auto"
                ),
            ],
            className="mb-2",
        ),

        dbc.Modal(  
            [
                dbc.ModalHeader(
                    html.H4('Save Success')
                ),
                dbc.ModalBody(
                'Message here! Edit me please!'
                ),
                    dbc.ModalFooter(
                        dbc.Button(
                        "Proceed",
                            href='/register_user' # Clicking this would lead to a change of pages
                    )
                )
            ],
            centered=True,
            id='registeruser_successmodal',
            backdrop='static' # Dialog box does not go away if you click at the background
        )
        
    ],
    className="g-2",
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
                    html.H1("CREATE NEW USER"),
                    html.Hr(),
                    dbc.Alert(id='registeruser_alert', is_open=False), # For feedback purpose
                    form,
                     
                ],
                width=8, style={'marginLeft': '15px'}
                
                )
            ]
        ),
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
    [
        Output('registeruser_alert', 'color'),
        Output('registeruser_alert', 'children'),
        Output('registeruser_alert', 'is_open'),
        Output('registeruser_successmodal', 'is_open')
    ],
    [
        Input('save_button', 'n_clicks')
    ],
    [
        State('user_fname', 'value'),
        State('user_mname', 'value'),
        State('user_sname', 'value'),
        State('user_livedname', 'value'),
        State('user_sex', 'value'),    
        State('user_bday', 'date'),
        State('user_phone_num', 'value'),
        State('user_id_num', 'value'),
        State('user_office', 'value'),
        State('user_position', 'value'),
        State('user_email', 'value'),
        State('user_password', 'value'),  
        State('confirm_password', 'value')  
    ]
)
 

def register_user(submitbtn, fname, mname, sname, livedname, 
                  sex, bday, phone_num, id_num, 
                  office, position, email, password, confirm_password):
    ctx = dash.callback_context
    # Check if the callback was triggered by the 'save_button'
    if not ctx.triggered:
        raise PreventUpdate

    eventid = ctx.triggered[0]['prop_id'].split('.')[0]
    if eventid != 'save_button' or not submitbtn:
        raise PreventUpdate

    # Initialize the alert variables
    alert_open = False
    modal_open = False
    alert_color = ''
    alert_text = ''

    # Validate password and confirmation password
    if not password:
        alert_open = True
        alert_color = 'danger'
        alert_text = 'Check your inputs. Please supply the password.'
        return [alert_color, alert_text, alert_open, modal_open]

    if not confirm_password:
        alert_open = True
        alert_color = 'danger'
        alert_text = 'Check your inputs. Please supply the confirm password.'
        return [alert_color, alert_text, alert_open, modal_open]

    if password != confirm_password:
        alert_open = True
        alert_color = 'danger'
        alert_text = 'Passwords do not match. Please try again.'
        return [alert_color, alert_text, alert_open, modal_open]

    # Hash the password
    hashed_password = hash_password(password)

    # Default values
    user_access_type = 1
    user_acc_status = 1
    user_profile_pic = None  # This will be interpreted as NULL in SQL






    # SQL query to insert data
    sql = """
        INSERT INTO maindashboard.users (
            user_fname, user_mname, user_sname, user_livedname, 
            user_sex, user_bday, user_phone_num, user_id_num, 
            user_office, user_position, user_email, user_password, 
            user_access_type, user_acc_status, user_profile_pic
        )
        VALUES (
            %s, %s, %s, %s, 
            %s, %s, %s, %s, 
            %s, %s, %s, %s, 
            %s, %s, %s
        )
    """

    default_acc_status = 1   
    values = (
        fname, mname, sname, livedname, 
        sex, bday, phone_num, id_num, 
        office, position, email, hashed_password, 
        user_access_type, user_acc_status, user_profile_pic
    )

    try: 
        db.modifydatabase(sql, values)
        alert_color = 'success'
        alert_open = True
        alert_text = "User registered successfully."

    except Exception as e:
        alert_color = 'danger'
        alert_open = True
        alert_text = f"Error in registration: {e}"

    return [alert_color, alert_text, alert_open, modal_open]