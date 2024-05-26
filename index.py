from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import webbrowser 

from app import app
from apps import commonmodules as cm
from apps import home


from apps.maindashboard import homepage, user_profile, register_user, search_users, password, about_TINQAD
from apps.admin import administration_dashboard, record_expenses, training_instructions, training_documents, add_expenses, training_record
from apps.iqa import iqa_dashboard, more_details, acad_heads_directory, acadheads_profile
from apps.eqa import eqa_dashboard, assessment_reports, assessment_details, accreditation_tracker, program_list, program_details, sar_details
from apps.km import THEworld_rankings, SDGimpact_rankings, SDG_submission, SDG_revision, add_criteria, SDG_evidencelist
from apps.qaofficers import qa_directory, training_list, qaofficers_profile, training_details, view_list

 
CONTENT_STYLE = {
    "margin-top": "4em",
    "margin-left": "1em",
    "margin-right": "1em",
    "padding": "1em 1em",
}

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=True),
        cm.navbar,
        html.Div(id='page-content', style=CONTENT_STYLE),
        html.Link(rel='icon', href='/assets/icons/TINQAD.png')
    ]
)


@app.callback(
    [
        Output('page-content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)




def displaypage (pathname):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if eventid == 'url': 
            if pathname == '/' or pathname == '/home':
                returnlayout = home.layout

            #maindashboard
            elif pathname == '/homepage':
                returnlayout = homepage.layout
            elif pathname == '/profile':
                returnlayout = user_profile.layout  
            elif pathname == '/register_user':
                returnlayout = register_user.layout
            elif pathname == '/search_users':
                returnlayout = search_users.layout
            elif pathname == '/change-password':
                returnlayout = password.layout
            elif pathname == '/About_TINQAD':
                returnlayout = about_TINQAD.layout

            #admin
            elif pathname == '/administration_dashboard':
                returnlayout = administration_dashboard.layout
            elif pathname == '/record_expenses':
                returnlayout = record_expenses.layout
            elif pathname == '/record_expenses/add_expense':
                returnlayout = add_expenses.layout
            elif pathname == '/training_instructions':
                returnlayout = training_instructions.layout
            elif pathname == '/training_documents':
                returnlayout = training_documents.layout
            elif pathname == '/training_record':
                returnlayout = training_record.layout
                
            #IQA
            elif pathname == '/iqa_dashboard':
                returnlayout = iqa_dashboard.layout
            elif pathname == '/dashboard/more_details':
                returnlayout = more_details.layout  
            elif pathname == '/acad_heads_directory':
                returnlayout = acad_heads_directory.layout
            elif pathname == '/acadheads_profile':
                returnlayout = acadheads_profile.layout
            
            
            #EQA
            elif pathname == '/eqa_dashboard':
                returnlayout = eqa_dashboard.layout
            elif pathname == '/assessment_reports':
                returnlayout = assessment_reports.layout
            elif pathname == '/assessmentreports/assessment_details':
                returnlayout = assessment_details.layout
            elif pathname == '/assessmentreports/sar_details':
                returnlayout = sar_details.layout
            elif pathname == '/accreditation_tracker':
                returnlayout = accreditation_tracker.layout
            elif pathname == '/program_list':
                returnlayout = program_list.layout
            elif pathname == '/program_details':
                returnlayout = program_details.layout

            #KM
            #elif pathname == '/km_dashboard':
                #returnlayout = km_dashboard.layout 
            elif pathname == '/add_criteria':
                returnlayout = add_criteria.layout 
            elif pathname == '/THEworld_rankings':
                returnlayout = THEworld_rankings.layout 
            elif pathname == '/SDGimpact_rankings':
                returnlayout = SDGimpact_rankings.layout 
            elif pathname == '/SDGimpactrankings/SDG_submission':
                returnlayout = SDG_submission.layout 
            elif pathname == '/SDGimpactrankings/SDG_revision':
                returnlayout = SDG_revision.layout 
            elif pathname == '/SDG_evidencelist':
                returnlayout = SDG_evidencelist.layout 
            #elif pathname == '/QSworld_rankings':
                #returnlayout = QSworld_rankings.layout 

            
            #QA Officers 
            elif pathname == '/QAOfficers_dashboard':
                returnlayout = training_list.layout
            elif pathname == '/qaofficers_profile':
                returnlayout = qaofficers_profile.layout  
            elif pathname == '/QAOfficers/addtraining':
                returnlayout = training_details.layout
            elif pathname == '/QAOfficers/datalist':
                returnlayout = view_list.layout
            elif pathname == '/QAOfficers_directory':
                returnlayout = qa_directory.layout

            else:
                returnlayout = 'error404'
    
            return [returnlayout]
    
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)
