import streamlit as st

st.set_page_config(
    page_title="ECS Digital Platform Prototype",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st

# Simple login credentials
USERNAME = "ecs_demo"
PASSWORD = "ecs2026"

# Session state to track login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login screen
if not st.session_state.authenticated:
    st.title("ECS Stakeholder Platform Access")

    st.write("Please enter credentials to access the ECS prototype platform.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()
st.info("This platform is an illustrative prototype for stakeholder engagement and capacity building for the Emissions Compliance System (ECS).")

import os
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="ECS Platform", layout="wide")

FEEDBACK_FILE = "feedback_submissions.xlsx"
SUPPORT_FILE = "support_requests.xlsx"


def save_to_excel(file_name, new_row):
    new_df = pd.DataFrame([new_row])

    if os.path.exists(file_name):
        existing_df = pd.read_excel(file_name)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        updated_df = new_df

    updated_df.to_excel(file_name, index=False)


def load_excel(file_name):
    if os.path.exists(file_name):
        return pd.read_excel(file_name)
    return pd.DataFrame()


st.title("ECS Digital Platform Prototype")
st.write("Prototype for stakeholder engagement and capacity building for the Emissions Compliance System (ECS).")

st.sidebar.markdown("---")

user_role = st.sidebar.selectbox(
    "Login as",
    ["Public User", "Covered Entity", "Regulator", "Verifier", "Administrator"],
    key="user_role_selector",
)

st.sidebar.markdown("---")

role_access = {
    "Public User": [
        "Home",
        "Information Portal",
        "Capacity Building Hub",
    ],
    "Covered Entity": [
        "Home",
        "Information Portal",
        "Consultation Portal",
        "Simulation Tool",
        "Capacity Building Hub",
        "Registry Technical Support",
    ],
    "Regulator": [
        "Home",
        "Information Portal",
        "Consultation Portal",
        "Simulation Tool",
        "Capacity Building Hub",
        "Registry Technical Support",
        "Stakeholder Dashboard",
    ],
    "Verifier": [
        "Home",
        "Information Portal",
        "Consultation Portal",
        "Capacity Building Hub",
        "Registry Technical Support",
    ],
    "Administrator": [
        "Home",
        "Information Portal",
        "Consultation Portal",
        "Simulation Tool",
        "Capacity Building Hub",
        "Registry Technical Support",
        "Stakeholder Dashboard",
    ],
}

allowed_modules = role_access[user_role]

module = st.sidebar.radio(
    "Select Module",
    allowed_modules,
    key="main_module_selector",
)

# Default subsection values
info_section = None
consultation_section = None
simulation_section = None
capacity_section = None
support_section = None
dashboard_section = None

if module == "Information Portal":
    with st.sidebar.expander("Information Portal Sections", expanded=True):
        info_section = st.radio(
            "Information Portal Sections",
            [
                "What is the ECS?",
                "How the ECS Works",
                "ECS Legislative Framework",
                "ECS Timeline",
                "Monitoring, Reporting and Verification (MRV)",
                "Registry and Market Infrastructure",
                "Market Information and Data",
                "Documentation Library",
                "FAQ and Helpdesk",
            ],
            key="info_section_selector",
            label_visibility="collapsed",
        )

elif module == "Consultation Portal":
    with st.sidebar.expander("Consultation Portal Sections", expanded=True):
        consultation_section = st.radio(
            "Consultation Portal Sections",
            [
                "Feedback Submission",
                "Stakeholder Engagement Schedule",
                "Engagement Timeline",
            ],
            key="consultation_section_selector",
            label_visibility="collapsed",
        )

elif module == "Simulation Tool":
    with st.sidebar.expander("Simulation Sections", expanded=True):
        simulation_section = st.radio(
            "Simulation Sections",
              [
        "Firm Compliance Strategy",
        "Allowance Trading Market",
        "Carbon Price Pathways",
        "Sector Decarbonization Pathways",
        "Allowance Market Balance",
        "Carbon Allowance Trading Des"
    ],
            key="simulation_section_selector",
            label_visibility="collapsed",
        )

elif module == "Capacity Building Hub":
    with st.sidebar.expander("Capacity Building Sections", expanded=True):
        capacity_section = st.radio(
            "Capacity Building Sections",
            [
                "Overview",
                "Who is this Training For?",
                "Participant Learning Path",
                "Training Modules",
                "Training Resources",
                "Practice Tools",
                "Simulation User Guide",
                "Disclaimer",
            ],
            key="capacity_section_selector",
            label_visibility="collapsed",
        )

elif module == "Registry Technical Support":
    with st.sidebar.expander("Support Sections", expanded=True):
        support_section = st.radio(
            "Support Sections",
            [
                "Submit Support Request",
                "Support Request Log",
            ],
            key="support_section_selector",
            label_visibility="collapsed",
        )

elif module == "Stakeholder Dashboard":
    with st.sidebar.expander("Dashboard Sections", expanded=True):
        dashboard_section = st.radio(
            "Dashboard Sections",
            [
                "Overview",
                "Feedback Analytics",
                "Support Analytics",
            ],
            key="dashboard_section_selector",
            label_visibility="collapsed",
        )

if module == "Home":
    st.header("Welcome")

    st.write(
        "The ECS Digital Platform Prototype is an illustrative stakeholder-facing platform "
        "designed to demonstrate how an Emissions Compliance System (ECS) could integrate "
        "policy information, consultation, market training, capacity building, technical support, "
        "and stakeholder analytics within a single digital interface."
    )

    st.info(
        "Illustrative prototype only. This platform is intended to support engagement, capacity building, "
        "and user understanding. It does not represent a final regulatory framework or operational system."
    )

    top_col1, top_col2, top_col3 = st.columns(3)
    top_col1.metric("Core Modules", "6")
    top_col2.metric("Training Components", "5+")
    top_col3.metric("Engagement Functions", "Consultation, Support, Analytics")

    st.markdown("---")
    st.subheader("Platform Structure")

    module_col1, module_col2 = st.columns(2)

    with module_col1:
        st.markdown("### 1. Information Portal")
        st.write(
            "Provides structured policy, regulatory, and technical information designed to help "
            "stakeholders understand the ECS and its institutional, legal, and operational context."
        )

        st.markdown("**Key Sections**")
        st.write("- What is the ECS?")
        st.write("- How the ECS Works")
        st.write("- ECS Legislative Framework")
        st.write("- ECS Timeline")
        st.write("- Monitoring, Reporting and Verification (MRV)")

        st.write("- Registry and Market Infrastructure")
        st.write("- Consultation and Stakeholder Engagement")
        st.write("- Market Information and Data")
        st.write("- Documentation Library")
        st.write("- FAQ and Helpdesk")

    with module_col2:
        st.markdown("### 2. Consultation Portal")
        st.write(
            "Supports stakeholder participation by enabling structured feedback submission, "
            "illustrative engagement scheduling, and visibility on consultation activities."
        )

        st.markdown("**Key Sections**")
        st.write("- Feedback Submission")
        st.write("- Stakeholder Engagement Schedule")
        st.write("- Engagement Timeline")

        st.markdown("### 3. Carbon Market Training Simulator")
        st.write(
            "Provides a structured training environment for exploring compliance decisions, "
            "carbon pricing, allowance trading, sector pathways, and market balance."
        )

        st.markdown("**Learning Steps**")
        st.write("- Firm Compliance Strategy")
        st.write("- Allowance Trading Market")
        st.write("- Carbon Price Pathways")
        st.write("- Sector Decarbonization Pathways")
        st.write("- Allowance Market Balance")

    st.markdown("---")

    module_col3, module_col4 = st.columns(2)

    with module_col3:
        st.markdown("### 4. Capacity Building Hub")
        st.write(
            "Provides training and readiness resources for stakeholder groups participating "
            "in or supporting the ECS."
        )

        st.markdown("**Key Sections**")
        st.write("- Who is this Training For?")
        st.write("- Participant Learning Path")
        st.write("- Training Modules")
        st.write("- Training Resources")
        st.write("- Practice Tools")
        st.write("- Simulation User Guide")
        st.write("- Disclaimer")

    with module_col4:
        st.markdown("### 5. Registry Technical Support")
        st.write(
            "Supports participants with registry and technical assistance needs through "
            "illustrative support submission and issue tracking functionality."
        )

        st.markdown("**Key Functions**")
        st.write("- Technical support request submission")
        st.write("- Registry issue logging")
        st.write("- Support request tracking")

        st.markdown("### 6. Stakeholder Dashboard")
        st.write(
            "Provides an analytics view of stakeholder participation, consultation themes, "
            "support requests, and engagement trends."
        )

        st.markdown("**Key Analytics**")
        st.write("- Stakeholder participation by sector")
        st.write("- Feedback analytics")
        st.write("- Policy issue heatmap")
        st.write("- Engagement tracking by phase")
        st.write("- Support request analysis")

    st.markdown("---")
    st.subheader("Illustrative Stakeholder Journey")

    journey_df = pd.DataFrame(
        {
            "Stage": [
                "1. Learn",
                "2. Engage",
                "3. Practice",
                "4. Prepare",
                "5. Seek Support",
                "6. Review Insights",
            ],
            "Illustrative User Journey": [
                "Stakeholders access the Information Portal to understand ECS objectives, rules, and market structure.",
                "Stakeholders participate through the Consultation Portal by reviewing engagement schedules and submitting feedback.",
                "Users explore compliance, carbon pricing, and trading concepts in the Carbon Market Training Simulator.",
                "Stakeholders strengthen readiness through the Capacity Building Hub and its training pathway.",
                "Users submit registry and technical issues through Registry Technical Support.",
                "Regulators and administrators review stakeholder participation and issue trends in the Stakeholder Dashboard.",
            ],
        }
    )

    st.dataframe(journey_df, width="stretch")

    st.markdown("### Professional Positioning")
    st.write(
        "This platform is structured to resemble a regulator-style stakeholder interface, "
        "combining policy transparency, consultation, capacity building, simulation-based learning, "
        "technical support, and engagement analytics in one integrated prototype environment."
    )
elif module == "Information Portal":
    st.header("Information Portal")

    st.write(
        "This section provides an illustrative information portal structure for an "
        "Emissions Compliance System (ECS). It is designed to demonstrate how a "
        "stakeholder-facing portal could organize core policy, regulatory, and technical information."
    )

    st.info(
        "Illustrative prototype only. The content below is designed for engagement, "
        "capacity building, and user understanding, and does not represent a final regulatory framework."
    )

    portal_tab_1, portal_tab_2, portal_tab_3, portal_tab_4, portal_tab_5 = st.tabs(
        [
            "System Overview",
            "Policy & Legal Framework",
            "MRV & Registry",
            "Engagement & Market Data",
            "Library & Helpdesk",
        ]
    )

    # ---------------------------------------------------
    # Tab 1: System Overview
    # ---------------------------------------------------
    with portal_tab_1:
        st.subheader("System Overview")

        subtab1, subtab2, subtab3 = st.tabs(
            ["What is the ECS?", "How the ECS Works", "ECS Timeline"]
        )

        with subtab1:
            st.markdown("### What is the ECS?")
            st.write(
                "The ECS is an illustrative emissions compliance system designed to support "
                "emissions management, improve transparency, and strengthen incentives for lower-carbon action."
            )

            st.markdown("**Objectives of the ECS**")
            st.write(
                "The ECS may support emissions transparency, create incentives for emissions reductions, "
                "encourage operational efficiency, and strengthen alignment with broader climate and industrial goals."
            )

            st.markdown("**Role in Climate Policy**")
            st.write(
                "The ECS can be one part of a wider climate policy framework, alongside energy transition measures, "
                "industrial modernization efforts, and environmental regulation."
            )

            st.markdown("**Covered Sectors**")
            st.write(
                "Illustrative coverage may include power and utilities, industrial manufacturing, "
                "petrochemical value chains, refining and processing, cement and construction materials, "
                "and metals and materials."
            )

            st.markdown("**Expected Environmental Outcomes**")
            st.write(
                "Expected outcomes may include improved emissions visibility, stronger incentives for abatement, "
                "support for lower-carbon investment decisions, and gradual progress toward emissions reduction objectives."
            )

        with subtab2:
            st.markdown("### How the ECS Works")

            st.markdown("**Emissions Cap**")
            st.write(
                "An illustrative ECS may define an emissions control framework for covered participants "
                "over a compliance period."
            )

            st.markdown("**Allowances**")
            st.write(
                "Allowances represent the right to emit a specified quantity of emissions. "
                "These may be allocated, distributed, or otherwise made available to participants."
            )

            st.markdown("**Trading Mechanism**")
            st.write(
                "If one participant has more allowances than it needs, it may have a surplus position. "
                "If another participant has fewer allowances than required, it may need to acquire "
                "additional allowances or reduce emissions."
            )

            st.markdown("**Compliance Cycle**")
            st.write(
                "A standard compliance cycle generally includes monitoring emissions, reporting verified data, "
                "reviewing allowance positions, and surrendering allowances where required."
            )

            st.markdown("**Role of Regulated Installations**")
            st.write(
                "Regulated installations are responsible for tracking emissions, maintaining records, "
                "submitting reports, and meeting compliance obligations under the system."
            )

        with subtab3:
            st.markdown("### ECS Timeline")

            timeline_df = pd.DataFrame(
                {
                    "Stage": ["Design Phase", "Pilot Phase", "Operational Phase"],
                    "Illustrative Description": [
                        "Policy design, consultation, legal structuring, and technical preparation.",
                        "Limited implementation, stakeholder onboarding, testing, and refinement.",
                        "Full operational launch, regular compliance cycles, and market functioning.",
                    ],
                }
            )

            st.dataframe(timeline_df, width="stretch")

            st.write(
                "This section helps stakeholders understand where the system is in its development journey "
                "and what activities may be expected next."
            )

    # ---------------------------------------------------
    # Tab 2: Policy & Legal Framework
    # ---------------------------------------------------
    with portal_tab_2:
        st.subheader("Policy & Legal Framework")

        subtab1, subtab2 = st.tabs(
            ["ECS Legislative Framework", "Consultation and Stakeholder Engagement"]
        )

        with subtab1:
            st.markdown("### ECS Legislative Framework")

            st.markdown("**ECS Regulations**")
            st.write(
                "This section would normally present the main regulatory instruments that establish "
                "the ECS and define its operational requirements."
            )

            st.markdown("**Legal Basis**")
            st.write(
                "The legal basis would describe the authority under which the ECS is established, "
                "including relevant laws, decrees, regulations, or implementing decisions."
            )

            st.markdown("**Institutional Responsibilities**")
            st.write("- Ministry roles")
            st.write("- Regulatory authority")
            st.write("- Market regulator")
            st.write("- Registry administrator")
            st.write("- Compliance oversight body")

            st.markdown("**Compliance Requirements**")
            st.write(
                "Compliance requirements may include emissions monitoring, reporting, verification, "
                "recordkeeping, and timely surrender of allowances."
            )

        with subtab2:
            st.markdown("### Consultation and Stakeholder Engagement")

            st.markdown("**Consultation Papers**")
            st.write(
                "This section can include draft papers, concept notes, and public consultation materials."
            )

            st.markdown("**Policy Proposals**")
            st.write(
                "Stakeholders can review key design proposals and understand how policy options are evolving."
            )

            st.markdown("**Stakeholder Feedback Forms**")
            st.write(
                "Users may submit structured feedback through consultation forms and engagement channels."
            )

            st.markdown("**Workshop Materials**")
            st.write(
                "Presentation decks, workshop summaries, and training materials can be shared here "
                "to support transparency and awareness."
            )

    # ---------------------------------------------------
    # Tab 3: MRV & Registry
    # ---------------------------------------------------
    with portal_tab_3:
        st.subheader("MRV & Registry")

        subtab1, subtab2 = st.tabs(
            ["Monitoring, Reporting and Verification (MRV)", "Registry and Market Infrastructure"]
        )

        with subtab1:
            st.markdown("### Monitoring, Reporting and Verification (MRV)")

            st.markdown("**Monitoring Plans**")
            st.write(
                "Covered entities may be required to prepare monitoring plans describing how emissions "
                "are measured, recorded, and managed."
            )

            st.markdown("**Emissions Reporting**")
            st.write(
                "Participants may be required to submit emissions reports on a defined schedule "
                "using approved methodologies and templates."
            )

            st.markdown("**Third-Party Verification**")
            st.write(
                "Independent verification can support data quality, strengthen market confidence, "
                "and improve consistency in compliance reporting."
            )

            st.markdown("**Compliance Deadlines**")
            st.write(
                "This section would normally explain submission deadlines, reporting windows, "
                "verification timelines, and surrender deadlines."
            )

        with subtab2:
            st.markdown("### Registry and Market Infrastructure")

            st.markdown("**ECS Registry Accounts**")
            st.write(
                "Participants may need registry accounts to hold allowances, review balances, "
                "and complete compliance-related transactions."
            )

            st.markdown("**Allowance Transfers**")
            st.write(
                "The registry infrastructure can support the transfer of allowances between accounts "
                "in line with system rules."
            )

            st.markdown("**Surrendering Allowances**")
            st.write(
                "At the end of the compliance cycle, participants may be required to surrender "
                "allowances equal to verified emissions."
            )

            st.markdown("**Compliance Tracking**")
            st.write(
                "The market infrastructure can support tracking of account balances, transfers, "
                "and compliance status."
            )

    # ---------------------------------------------------
    # Tab 4: Engagement & Market Data
    # ---------------------------------------------------
    with portal_tab_4:
        st.subheader("Engagement & Market Data")

        subtab1, subtab2 = st.tabs(
            ["Market Information and Data", "Stakeholder Transparency"]
        )

        with subtab1:
            st.markdown("### Market Information and Data")

            market_df = pd.DataFrame(
                {
                    "Indicator": [
                        "Illustrative Emissions Data",
                        "Illustrative Allowance Price",
                        "Illustrative Sector Performance",
                        "Illustrative Compliance Statistics",
                    ],
                    "Example Value": [
                        "Available",
                        "$45/tCO2",
                        "Sector summaries published",
                        "Annual compliance summary",
                    ],
                }
            )

            st.dataframe(market_df, width="stretch")

            st.write(
                "Many ETS systems provide public-facing dashboards and data summaries to improve "
                "market transparency and stakeholder understanding."
            )

        with subtab2:
            st.markdown("### Stakeholder Transparency")
            st.write(
                "This portal structure is designed to support transparency by showing how policy information, "
                "technical guidance, stakeholder engagement, and market information can be presented in one place."
            )

    # ---------------------------------------------------
    # Tab 5: Library & Helpdesk
    # ---------------------------------------------------
    with portal_tab_5:
        st.subheader("Library & Helpdesk")

        subtab1, subtab2 = st.tabs(["Documentation Library", "FAQ and Helpdesk"])

        with subtab1:
            st.markdown("### Documentation Library")

            docs_df = pd.DataFrame(
                {
                    "Document Name": [
                        "ECS Overview Note",
                        "Draft ECS Regulations",
                        "MRV Guidelines",
                        "Registry User Manual",
                        "Allowance Transfer Procedure",
                        "Compliance Cycle Guidance",
                        "Consultation Paper 01",
                        "Consultation Paper 02",
                        "Workshop Presentation Deck",
                        "Sector Coverage Note",
                        "Illustrative Market Design Brief",
                        "FAQ and Helpdesk Guide",
                    ],
                    "Category": [
                        "Overview",
                        "Regulations",
                        "MRV",
                        "Registry",
                        "Registry",
                        "Compliance",
                        "Consultation",
                        "Consultation",
                        "Workshops",
                        "Policy Reports",
                        "Policy Reports",
                        "Support",
                    ],
                    "Document Type": [
                        "PDF",
                        "PDF",
                        "PDF",
                        "PDF",
                        "PDF",
                        "PDF",
                        "PDF",
                        "PDF",
                        "PPT",
                        "PDF",
                        "PDF",
                        "PDF",
                    ],
                    "Audience": [
                        "All Stakeholders",
                        "Regulated Entities",
                        "Regulated Entities",
                        "Regulated Entities",
                        "Regulated Entities",
                        "Regulated Entities",
                        "All Stakeholders",
                        "All Stakeholders",
                        "All Stakeholders",
                        "Policy Users",
                        "Policy Users",
                        "All Stakeholders",
                    ],
                    "Status": [
                        "Published",
                        "Draft",
                        "Published",
                        "Published",
                        "Published",
                        "Published",
                        "Published",
                        "Draft",
                        "Published",
                        "Published",
                        "Draft",
                        "Published",
                    ],
                    "Version": [
                        "v1.0",
                        "v0.9",
                        "v1.2",
                        "v1.0",
                        "v1.0",
                        "v1.1",
                        "v1.0",
                        "v0.8",
                        "v1.0",
                        "v1.0",
                        "v0.7",
                        "v1.0",
                    ],
                }
            )

            filter_col1, filter_col2 = st.columns(2)

            with filter_col1:
                selected_category = st.selectbox(
                    "Filter by Category",
                    [
                        "All",
                        "Overview",
                        "Regulations",
                        "MRV",
                        "Registry",
                        "Compliance",
                        "Consultation",
                        "Workshops",
                        "Policy Reports",
                        "Support",
                    ],
                    key="doc_category_filter",
                )

            with filter_col2:
                selected_audience = st.selectbox(
                    "Filter by Audience",
                    [
                        "All",
                        "All Stakeholders",
                        "Regulated Entities",
                        "Policy Users",
                    ],
                    key="doc_audience_filter",
                )

            filtered_docs = docs_df.copy()

            if selected_category != "All":
                filtered_docs = filtered_docs[filtered_docs["Category"] == selected_category]

            if selected_audience != "All":
                filtered_docs = filtered_docs[filtered_docs["Audience"] == selected_audience]

            st.dataframe(filtered_docs, width="stretch")

        with subtab2:
            st.markdown("### FAQ and Helpdesk")

            faq_items = {
                "What is a compliance cycle?":
                    "A compliance cycle is the period during which entities monitor, report, verify, and reconcile emissions obligations.",
                "What is MRV?":
                    "MRV refers to monitoring, reporting, and verification of emissions data.",
                "What is the registry used for?":
                    "The registry is used to manage accounts, track allowances, record transfers, and support compliance processes.",
                "Who can submit stakeholder feedback?":
                    "Illustratively, regulated entities, regulators, verifiers, industry associations, researchers, and other stakeholders may participate.",
                "Where can users get help?":
                    "Support may be provided through helpdesk channels, guidance materials, stakeholder contact points, and registry support services.",
            }

            for question, answer in faq_items.items():
                with st.expander(question):
                    st.write(answer)

            st.markdown("**Support Channels**")
            st.write("- Guidance materials")
            st.write("- Registry support channels")
            st.write("- Stakeholder contact points")
            st.write("- Consultation and helpdesk mechanisms")
elif module == "Consultation Portal":
    st.header("Consultation Portal")

    st.write(
        "This section supports stakeholder interaction, structured consultation, and engagement "
        "throughout the design, pilot, and operational development of the Emissions Compliance System (ECS)."
    )

    st.info(
        "Illustrative prototype only. The consultation structure, meeting cadence, and examples below "
        "are designed for stakeholder engagement and do not represent final institutional arrangements."
    )

    consultation_tab1, consultation_tab2, consultation_tab3 = st.tabs(
        [
            "Feedback Submission",
            "Stakeholder Engagement Schedule",
            "Engagement Timeline",
        ]
    )

    # ---------------------------------
    # Tab 1: Feedback Submission
    # ---------------------------------
    with consultation_tab1:
        st.subheader("Submit Feedback")

        st.write(
            "Stakeholders may provide structured feedback on ECS design, market functioning, "
            "compliance requirements, and technical implementation issues."
        )

        form_col1, form_col2 = st.columns([2, 1])

        with form_col1:
            with st.form("feedback_form"):
                name = st.text_input("Stakeholder Name")
                organization = st.text_input("Organization")

                sector = st.selectbox(
                    "Sector",
                    [
                        "Power and Utilities",
                        "Cement and Construction Materials",
                        "Petrochemical Value Chains",
                        "Steel and Manufacturing",
                        "Government / Public Institutions",
                        "Other",
                    ],
                )

                feedback_type = st.selectbox(
                    "Feedback Type",
                    [
                        "Policy Design",
                        "Market Functioning",
                        "Compliance Issue",
                        "Technical Issue",
                        "General Comment",
                    ],
                )

                pilot_phase = st.selectbox(
                    "Engagement Phase",
                    ["Design Phase", "Pilot Phase", "Operational Phase"],
                )

                comment = st.text_area("Comment")

                submitted = st.form_submit_button("Submit Feedback")

                if submitted:
                    feedback_row = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "stakeholder_name": name,
                        "organization": organization,
                        "sector": sector,
                        "feedback_type": feedback_type,
                        "comment": comment,
                        "pilot_phase": pilot_phase,
                    }

                    save_to_excel(FEEDBACK_FILE, feedback_row)
                    st.success("Feedback submitted and saved successfully.")

        with form_col2:
            st.markdown("**Consultation Focus Areas**")
            st.write("- Policy design")
            st.write("- Market functioning")
            st.write("- Compliance requirements")
            st.write("- Technical implementation")
            st.write("- Sector readiness")

        feedback_df = load_excel(FEEDBACK_FILE)
        if not feedback_df.empty:
            st.markdown("---")
            st.subheader("Submitted Feedback Records")
            st.dataframe(feedback_df, width="stretch")

    # ---------------------------------
    # Tab 2: Stakeholder Engagement Schedule
    # ---------------------------------
    with consultation_tab2:
        st.subheader("Stakeholder Engagement Schedule")

        st.write(
            "The ECS stakeholder engagement process includes regular meetings and consultations "
            "to ensure transparency, gather feedback, and support effective system design and implementation."
        )

        schedule_tab1, schedule_tab2, schedule_tab3, schedule_tab4 = st.tabs(
            [
                "Technical Working Group Meetings",
                "Sector Stakeholder Workshops",
                "Public Consultation Sessions",
                "Steering Committee Meetings",
            ]
        )

        with schedule_tab1:
            st.markdown("### Technical Working Group Meetings")
            st.write("**Frequency:** Monthly")
            st.write("**Participants:** Regulated sectors, technical experts, MRV specialists")

            st.markdown("**Purpose**")
            st.write("- Discuss technical aspects of ECS design")
            st.write("- Review MRV methodologies")
            st.write("- Address sector-specific concerns")

        with schedule_tab2:
            st.markdown("### Sector Stakeholder Workshops")
            st.write("**Frequency:** Quarterly")

            st.markdown("**Purpose**")
            st.write("- Present policy updates")
            st.write("- Discuss sector readiness")
            st.write("- Collect industry feedback")

            st.markdown("**Illustrative Sectors**")
            st.write("- Power and Utilities")
            st.write("- Cement and Construction")
            st.write("- Petrochemicals")
            st.write("- Steel and Manufacturing")

        with schedule_tab3:
            st.markdown("### Public Consultation Sessions")
            st.write("**Frequency:** At key policy milestones")

            st.markdown("**Purpose**")
            st.write("- Present draft policy documents")
            st.write("- Gather stakeholder input")
            st.write("- Ensure transparency in system design")

        with schedule_tab4:
            st.markdown("### Steering Committee Meetings")
            st.write("**Frequency:** As required")
            st.write("**Participants:** Senior government representatives, regulatory authorities, policy advisors")

            st.markdown("**Purpose**")
            st.write("- Review strategic decisions")
            st.write("- Approve major design elements")

        st.markdown("---")
        st.markdown("**Engagement Structure Summary**")

        engagement_df = pd.DataFrame(
            {
                "Engagement Format": [
                    "Technical Working Group Meetings",
                    "Sector Stakeholder Workshops",
                    "Public Consultation Sessions",
                    "Steering Committee Meetings",
                ],
                "Illustrative Frequency": [
                    "Monthly",
                    "Quarterly",
                    "At key policy milestones",
                    "As required",
                ],
                "Primary Purpose": [
                    "Technical design review and MRV discussion",
                    "Sector readiness discussion and feedback collection",
                    "Policy transparency and structured public input",
                    "Strategic review and major design decisions",
                ],
            }
        )

        st.dataframe(engagement_df, width="stretch")

    # ---------------------------------
    # Tab 3: Engagement Timeline
    # ---------------------------------
    with consultation_tab3:
        st.subheader("Example Engagement Timeline")

        timeline_col1, timeline_col2, timeline_col3 = st.columns(3)

        with timeline_col1:
            st.markdown("### Design Phase")
            st.write("- Monthly technical working group meetings")
            st.write("- Sector consultation workshops")

        with timeline_col2:
            st.markdown("### Pilot Phase")
            st.write("- Training sessions for regulated entities")
            st.write("- MRV readiness workshops")

        with timeline_col3:
            st.markdown("### Operational Phase")
            st.write("- Annual stakeholder forums")
            st.write("- Market performance review meetings")

        st.markdown("---")
        st.markdown("**Illustrative Timeline Summary**")

        timeline_df = pd.DataFrame(
            {
                "Phase": [
                    "Design Phase",
                    "Pilot Phase",
                    "Operational Phase",
                ],
                "Illustrative Engagement Activities": [
                    "Monthly technical working group meetings; sector consultation workshops",
                    "Training sessions for regulated entities; MRV readiness workshops",
                    "Annual stakeholder forums; market performance review meetings",
                ],
            }
        )

        st.dataframe(timeline_df, width="stretch")


        st.markdown("**Illustrative Best Practice Note**")
        st.write(
            "Most ETS-style programs include technical working groups, sector consultations, "
            "public consultation periods, and stakeholder forums as part of system development and implementation."
        )




elif module == "Simulation Tool":
    st.header("ECS Carbon Market Training Simulator")

    st.write(
        "This interactive simulator allows stakeholders to explore how an Emissions "
        "Compliance System (ECS) functions. Users can test compliance strategies, observe "
        "carbon price dynamics, explore emissions reduction pathways, and understand "
        "allowance market balance in a simplified training environment."
    )

    st.info(
        "This simulator is designed for training and stakeholder engagement purposes. "
        "Results are illustrative and do not represent real regulatory outcomes."
    )

    # -----------------------------
    # Reset button
    # -----------------------------
    sim_keys_to_clear = [
        "policy_scenario",
        "learning_step",
        "firm_sector",
        "firm_carbon_price",
        "firm_emissions",
        "firm_allowances",
        "firm_abatement_cost",
        "firm_abatement_amount",
        "market_carbon_price",
        "trajectory_start_year",
        "trajectory_end_year",
        "trajectory_initial_price",
        "trajectory_annual_increase",
        "pathway_sector",
        "pathway_baseline_emissions",
        "pathway_reduction_rate",
        "pathway_start_year",
        "pathway_end_year",
        "market_supply",
        "demand_power",
        "demand_cement",
        "demand_petrochem",
        "demand_metals",
        "trading_carbon_price",
        "trade_buyer",
        "trade_seller",
        "trade_quantity",
        "firms_data",
        "trade_log",
    ]

    if st.button("Reset Simulation"):
        for key in sim_keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

    # -----------------------------
    # Policy scenario selector
    # -----------------------------
    scenario = st.selectbox(
        "Policy Scenario",
        [
            "Conservative Carbon Price",
            "Accelerated Decarbonization",
            "Tight Cap Scenario",
            "Technology Breakthrough",
        ],
        key="policy_scenario",
    )

    scenario_defaults = {
        "Conservative Carbon Price": {
            "carbon_price": 35,
            "annual_increase": 3,
            "abatement_cost_multiplier": 1.0,
            "allowance_multiplier": 1.0,
            "reduction_rate": 4,
            "supply_multiplier": 1.05,
        },
        "Accelerated Decarbonization": {
            "carbon_price": 60,
            "annual_increase": 6,
            "abatement_cost_multiplier": 1.0,
            "allowance_multiplier": 0.92,
            "reduction_rate": 8,
            "supply_multiplier": 0.95,
        },
        "Tight Cap Scenario": {
            "carbon_price": 75,
            "annual_increase": 8,
            "abatement_cost_multiplier": 1.1,
            "allowance_multiplier": 0.85,
            "reduction_rate": 7,
            "supply_multiplier": 0.85,
        },
        "Technology Breakthrough": {
            "carbon_price": 55,
            "annual_increase": 4,
            "abatement_cost_multiplier": 0.7,
            "allowance_multiplier": 0.95,
            "reduction_rate": 10,
            "supply_multiplier": 0.95,
        },
    }

    selected_scenario = scenario_defaults[scenario]

    st.markdown("### Learning Journey")

    learning_step = st.radio(
        "Select Step",
        [
            "Step 1 — Firm Compliance Strategy",
            "Step 2 — Allowance Trading Market",
            "Step 3 — Carbon Price Pathways",
            "Step 4 — Sector Decarbonization Pathways",
            "Step 5 — Allowance Market Balance",
            "Step 6 — Carbon Allowance Trading Desk",
        ],
        horizontal=True,
        key="learning_step",
    )

    sector_descriptions = {
        "Power and Utilities": (
            "Typically the largest source of emissions in many ETS systems. "
            "Decarbonization options may include renewable electricity, fuel switching, "
            "efficiency improvements, and carbon capture."
        ),
        "Cement and Construction Materials": (
            "Often emissions-intensive due to process and fuel emissions. "
            "Decarbonization may involve clinker substitution, fuel switching, "
            "efficiency, and new low-carbon production pathways."
        ),
        "Metals and Materials": (
            "This sector may face high energy demand and process emissions. "
            "Transition options can include electrification, efficiency gains, and low-carbon inputs."
        ),
        "Petrochemical Value Chains": (
            "A complex industrial sector where emissions can arise across multiple value chains. "
            "Decarbonization may involve efficiency, process redesign, cleaner feedstocks, and innovation."
        ),
        "Refining and Processing": (
            "This sector may face both direct process emissions and indirect energy-related emissions. "
            "Transition strategies can include efficiency measures, fuel switching, and technology upgrades."
        ),
    }

    # -----------------------------
    # Step 1 — Firm Compliance Strategy
    # -----------------------------
    if learning_step == "Step 1 — Firm Compliance Strategy":
        st.subheader("Step 1 — Firm Compliance Strategy")

        col1, col2 = st.columns([1, 1])

        with col1:
            selected_sector = st.selectbox(
                "Illustrative Sector",
                list(sector_descriptions.keys()),
                key="firm_sector",
            )

            st.caption(sector_descriptions[selected_sector])

            default_price = selected_scenario["carbon_price"]
            default_allowances = int(80 * selected_scenario["allowance_multiplier"])
            default_abatement_cost = int(30 * selected_scenario["abatement_cost_multiplier"])

            carbon_price = st.slider(
                "Carbon Price ($/tCO2)",
                0,
                200,
                default_price,
                key="firm_carbon_price",
            )
            emissions = st.number_input(
                "Emissions (tCO2)",
                min_value=0,
                value=100,
                key="firm_emissions",
            )
            allowances = st.number_input(
                "Allowances Allocated",
                min_value=0,
                value=default_allowances,
                key="firm_allowances",
            )
            abatement_cost = st.number_input(
                "Abatement Cost ($/tCO2)",
                min_value=0,
                value=default_abatement_cost,
                key="firm_abatement_cost",
            )
            abatement_amount = st.number_input(
                "Potential Abatement Quantity (tCO2)",
                min_value=0,
                value=20,
                key="firm_abatement_amount",
            )

        shortfall_before = max(emissions - allowances, 0)
        surplus_before = max(allowances - emissions, 0)
        compliance_cost_before = shortfall_before * carbon_price

        actual_abatement = min(abatement_amount, emissions)
        emissions_after = max(emissions - actual_abatement, 0)
        shortfall_after = max(emissions_after - allowances, 0)
        surplus_after = max(allowances - emissions_after, 0)
        compliance_cost_after = shortfall_after * carbon_price
        abatement_total_cost = actual_abatement * abatement_cost
        total_cost_with_abatement = compliance_cost_after + abatement_total_cost
        sale_revenue_after = surplus_after * carbon_price

        with col2:
            st.subheader("Key Results")
            st.metric("Shortfall Before Abatement", f"{shortfall_before} tCO2")
            st.metric("Surplus Before Abatement", f"{surplus_before} tCO2")
            st.metric("Compliance Cost Before Abatement", f"${compliance_cost_before:,.2f}")
            st.metric("Total Cost With Abatement", f"${total_cost_with_abatement:,.2f}")

        chart_data = pd.DataFrame(
            {
                "Scenario": ["Without Abatement", "With Abatement"],
                "Cost": [compliance_cost_before, total_cost_with_abatement],
            }
        )

        fig = px.bar(
            chart_data,
            x="Scenario",
            y="Cost",
            title="Compliance Cost Comparison",
        )
        st.plotly_chart(fig, width="stretch")

        st.markdown("### Learning Insight")
        if shortfall_before == 0:
            if surplus_before > 0:
                st.success(
                    "This firm already holds more allowances than it needs. In an ETS-style market, "
                    "that surplus could create a potential selling opportunity."
                )
            else:
                st.success("This firm is exactly balanced and would not need to buy or sell allowances.")
        else:
            if abatement_cost < carbon_price:
                st.info(
                    "When carbon prices exceed abatement costs, firms are more likely to invest in "
                    "emissions reduction rather than purchasing allowances."
                )
            elif abatement_cost > carbon_price:
                st.warning(
                    "When abatement costs exceed carbon prices, firms may prefer to purchase allowances "
                    "instead of reducing emissions immediately."
                )
            else:
                st.write(
                    "At this point, the firm is broadly indifferent between abating and purchasing allowances."
                )

        st.markdown("### Scenario Summary")
        st.write(f"- Sector: **{selected_sector}**")
        st.write(f"- Emissions before abatement: **{emissions} tCO2**")
        st.write(f"- Emissions after abatement: **{emissions_after} tCO2**")
        st.write(f"- Allowances allocated: **{allowances}**")
        st.write(f"- Abatement undertaken: **{actual_abatement} tCO2**")
        st.write(f"- Carbon price: **${carbon_price}/tCO2**")
        st.write(f"- Surplus after abatement: **{surplus_after} allowances**")
        st.write(f"- Potential illustrative sale revenue: **${sale_revenue_after:,.2f}**")

    # -----------------------------
    # Step 2 — Allowance Trading Market
    # -----------------------------
    elif learning_step == "Step 2 — Allowance Trading Market":
        st.subheader("Step 2 — Allowance Trading Market")

        carbon_price_market = st.slider(
            "Illustrative Market Carbon Price ($/tCO2)",
            0,
            200,
            selected_scenario["carbon_price"],
            key="market_carbon_price",
        )

        allowance_multiplier = selected_scenario["allowance_multiplier"]

        market_df = pd.DataFrame(
            {
                "Firm": ["Firm A", "Firm B", "Firm C", "Firm D"],
                "Sector": [
                    "Power and Utilities",
                    "Cement and Construction Materials",
                    "Petrochemical Value Chains",
                    "Metals and Materials",
                ],
                "Emissions": [120, 90, 70, 110],
                "Allowances": [
                    int(100 * allowance_multiplier),
                    int(95 * allowance_multiplier),
                    int(85 * allowance_multiplier),
                    int(90 * allowance_multiplier),
                ],
                "Abatement Cost": [
                    int(55 * selected_scenario["abatement_cost_multiplier"]),
                    int(35 * selected_scenario["abatement_cost_multiplier"]),
                    int(80 * selected_scenario["abatement_cost_multiplier"]),
                    int(45 * selected_scenario["abatement_cost_multiplier"]),
                ],
            }
        )

        market_df["Position"] = market_df["Allowances"] - market_df["Emissions"]
        market_df["Status"] = market_df["Position"].apply(
            lambda x: "Seller" if x > 0 else ("Buyer" if x < 0 else "Balanced")
        )
        market_df["Shortfall"] = market_df["Position"].apply(lambda x: abs(x) if x < 0 else 0)
        market_df["Surplus"] = market_df["Position"].apply(lambda x: x if x > 0 else 0)
        market_df["Illustrative Compliance Cost"] = market_df["Shortfall"] * carbon_price_market

        st.dataframe(market_df, width="stretch")

        col1, col2 = st.columns(2)

        with col1:
            fig_status = px.bar(
                market_df,
                x="Firm",
                y="Position",
                color="Status",
                title="Allowance Deficit vs Surplus by Firm",
            )
            st.plotly_chart(fig_status, width="stretch")

        with col2:
            status_counts = market_df["Status"].value_counts().reset_index()
            status_counts.columns = ["Status", "Count"]
            fig_market = px.bar(
                status_counts,
                x="Status",
                y="Count",
                title="Market Participants: Buyers vs Sellers",
            )
            st.plotly_chart(fig_market, width="stretch")

        st.markdown("### Learning Insight")
        st.info(
            "Firms with allowance surpluses become potential sellers, while firms with shortfalls "
            "become potential buyers. This is the core market dynamic of a cap-and-trade style system."
        )

    # -----------------------------
    # Step 3 — Carbon Price Pathways
    # -----------------------------
    elif learning_step == "Step 3 — Carbon Price Pathways":
        st.subheader("Step 3 — Carbon Price Pathways")

        col1, col2 = st.columns(2)

        with col1:
            start_year = st.number_input(
                "Start Year",
                min_value=2025,
                max_value=2050,
                value=2027,
                key="trajectory_start_year",
            )
            end_year = st.number_input(
                "End Year",
                min_value=2026,
                max_value=2060,
                value=2035,
                key="trajectory_end_year",
            )
            initial_price = st.number_input(
                "Initial Carbon Price ($/tCO2)",
                min_value=0,
                value=selected_scenario["carbon_price"],
                key="trajectory_initial_price",
            )
            annual_increase = st.number_input(
                "Annual Price Increase ($/tCO2)",
                min_value=0,
                value=selected_scenario["annual_increase"],
                key="trajectory_annual_increase",
            )

        if end_year <= start_year:
            st.warning("End Year must be greater than Start Year.")
        else:
            years = list(range(start_year, end_year + 1))
            prices = [initial_price + annual_increase * (year - start_year) for year in years]

            trajectory_df = pd.DataFrame(
                {
                    "Year": years,
                    "Carbon Price": prices,
                }
            )

            with col2:
                st.metric("Starting Price", f"${initial_price}/tCO2")
                st.metric("Ending Price", f"${prices[-1]}/tCO2")
                st.metric("Years Covered", len(years))

            fig_price = px.line(
                trajectory_df,
                x="Year",
                y="Carbon Price",
                markers=True,
                title="Illustrative Carbon Price Path",
            )
            st.plotly_chart(fig_price, width="stretch")
            st.dataframe(trajectory_df, width="stretch")

            st.markdown("### Learning Insight")
            st.info(
                "A rising carbon price path strengthens the long-term investment signal. "
                "This can influence fuel choices, technology planning, and the timing of abatement decisions."
            )

    # -----------------------------
    # Step 4 — Sector Decarbonization Pathways
    # -----------------------------
    elif learning_step == "Step 4 — Sector Decarbonization Pathways":
        st.subheader("Step 4 — Sector Decarbonization Pathways")

        col1, col2 = st.columns(2)

        with col1:
            pathway_sector = st.selectbox(
                "Sector",
                list(sector_descriptions.keys()),
                key="pathway_sector",
            )

            st.caption(sector_descriptions[pathway_sector])

            baseline_emissions = st.number_input(
                "Baseline Emissions (tCO2)",
                min_value=0,
                value=1000,
                key="pathway_baseline_emissions",
            )
            annual_reduction_rate = st.slider(
                "Annual Reduction Rate (%)",
                0,
                20,
                selected_scenario["reduction_rate"],
                key="pathway_reduction_rate",
            )
            start_year_path = st.number_input(
                "Pathway Start Year",
                min_value=2025,
                max_value=2050,
                value=2027,
                key="pathway_start_year",
            )
            end_year_path = st.number_input(
                "Pathway End Year",
                min_value=2026,
                max_value=2060,
                value=2035,
                key="pathway_end_year",
            )

        if end_year_path <= start_year_path:
            st.warning("Pathway End Year must be greater than Pathway Start Year.")
        else:
            years = list(range(start_year_path, end_year_path + 1))
            emissions_path = []
            current_emissions = baseline_emissions

            for year in years:
                emissions_path.append(current_emissions)
                current_emissions = current_emissions * (1 - annual_reduction_rate / 100)

            pathway_df = pd.DataFrame(
                {
                    "Year": years,
                    "Emissions": emissions_path,
                    "Sector": pathway_sector,
                }
            )

            cumulative_reduction = baseline_emissions - emissions_path[-1]

            with col2:
                st.metric("Baseline Emissions", f"{baseline_emissions:,.0f} tCO2")
                st.metric("Final Year Emissions", f"{emissions_path[-1]:,.0f} tCO2")
                st.metric("Illustrative Reduction", f"{cumulative_reduction:,.0f} tCO2")

            fig_path = px.line(
                pathway_df,
                x="Year",
                y="Emissions",
                markers=True,
                title=f"Illustrative Emissions Pathway: {pathway_sector}",
            )
            st.plotly_chart(fig_path, width="stretch")
            st.dataframe(pathway_df, width="stretch")

            st.markdown("### Learning Insight")
            st.info(
                "Sector pathways help stakeholders understand the pace of transition required "
                "under different policy assumptions and technology conditions."
            )

    # -----------------------------
    # Step 5 — Allowance Market Balance
    # -----------------------------
    elif learning_step == "Step 5 — Allowance Market Balance":
        st.subheader("Step 5 — Allowance Market Balance")

        col1, col2 = st.columns(2)

        with col1:
            total_supply = st.number_input(
                "Total Allowance Supply",
                min_value=0,
                value=int(400 * selected_scenario["supply_multiplier"]),
                key="market_supply",
            )
            demand_power = st.number_input(
                "Demand: Power and Utilities",
                min_value=0,
                value=120,
                key="demand_power",
            )
            demand_cement = st.number_input(
                "Demand: Cement and Construction Materials",
                min_value=0,
                value=90,
                key="demand_cement",
            )
            demand_petrochem = st.number_input(
                "Demand: Petrochemical Value Chains",
                min_value=0,
                value=100,
                key="demand_petrochem",
            )
            demand_metals = st.number_input(
                "Demand: Metals and Materials",
                min_value=0,
                value=110,
                key="demand_metals",
            )

        total_demand = demand_power + demand_cement + demand_petrochem + demand_metals
        market_gap = total_supply - total_demand

        with col2:
            st.metric("Total Supply", f"{total_supply:,.0f}")
            st.metric("Total Demand", f"{total_demand:,.0f}")
            st.metric("Market Balance (Supply - Demand)", f"{market_gap:,.0f}")

        supply_demand_df = pd.DataFrame(
            {
                "Category": [
                    "Allowance Supply",
                    "Power and Utilities Demand",
                    "Cement Demand",
                    "Petrochemicals Demand",
                    "Metals Demand",
                    "Total Demand",
                ],
                "Value": [
                    total_supply,
                    demand_power,
                    demand_cement,
                    demand_petrochem,
                    demand_metals,
                    total_demand,
                ],
            }
        )

        fig_balance = px.bar(
            supply_demand_df,
            x="Category",
            y="Value",
            title="Illustrative Allowance Supply and Demand",
        )
        st.plotly_chart(fig_balance, width="stretch")

        st.markdown("### Learning Insight")
        if market_gap > 0:
            st.success(
                "Allowance supply exceeds demand. In simplified terms, this may reduce scarcity pressure in the market."
            )
        elif market_gap < 0:
            st.warning(
                "Demand exceeds allowance supply. In simplified terms, this may increase scarcity and price pressure."
            )
        else:
            st.info("Allowance supply and demand are balanced in this illustrative scenario.")

    # -----------------------------
    # Step 6 — Carbon Allowance Trading Desk
    # -----------------------------
    elif learning_step == "Step 6 — Carbon Allowance Trading Desk":
        st.subheader("Step 6 — Carbon Allowance Trading Desk")
        st.caption("Illustrative training interface for carbon allowance trading.")

        if "firms_data" not in st.session_state:
            st.session_state.firms_data = pd.DataFrame({
                "Firm": ["Cement Co.", "Steel Co.", "Power Co.", "Petrochem Co."],
                "Sector": ["Cement", "Steel", "Power", "Petrochemicals"],
                "Emissions": [120, 90, 150, 110],
                "Allowances": [100, 110, 130, 120]
            })
            st.session_state.firms_data["Position"] = (
                st.session_state.firms_data["Allowances"]
                - st.session_state.firms_data["Emissions"]
            )

        if "trade_log" not in st.session_state:
            st.session_state.trade_log = []

        firms_data = st.session_state.firms_data

        st.markdown("### Firm Positions")
        st.dataframe(firms_data, width="stretch")

        carbon_price_trade = st.slider(
            "Current Carbon Price ($/tCO2)",
            20,
            150,
            selected_scenario["carbon_price"],
            key="trading_carbon_price",
        )

        buyers = firms_data[firms_data["Position"] < 0]["Firm"].tolist()
        sellers = firms_data[firms_data["Position"] > 0]["Firm"].tolist()

        st.markdown("### Execute Trade")

        if buyers and sellers:
            buyer = st.selectbox("Buyer Firm", buyers, key="trade_buyer")
            seller = st.selectbox("Seller Firm", sellers, key="trade_seller")

            buyer_gap = abs(
                firms_data.loc[firms_data["Firm"] == buyer, "Position"].values[0]
            )
            seller_surplus = firms_data.loc[
                firms_data["Firm"] == seller, "Position"
            ].values[0]

            max_trade = int(min(buyer_gap, seller_surplus))

            quantity = st.number_input(
                "Allowances to Trade",
                min_value=1,
                max_value=max_trade if max_trade > 0 else 1,
                value=1,
                key="trade_quantity",
            )

            if st.button("Execute Trade"):
                buyer_idx = firms_data[firms_data["Firm"] == buyer].index[0]
                seller_idx = firms_data[firms_data["Firm"] == seller].index[0]

                st.session_state.firms_data.loc[buyer_idx, "Allowances"] += quantity
                st.session_state.firms_data.loc[seller_idx, "Allowances"] -= quantity

                st.session_state.firms_data["Position"] = (
                    st.session_state.firms_data["Allowances"]
                    - st.session_state.firms_data["Emissions"]
                )

                st.session_state.trade_log.append({
                    "Buyer": buyer,
                    "Seller": seller,
                    "Quantity": quantity,
                    "Price": carbon_price_trade,
                    "Value": quantity * carbon_price_trade,
                })

                st.success(
                    f"Illustrative trade executed: {buyer} purchased {quantity} allowances from {seller}."
                )
                st.rerun()
        else:
            st.warning("No valid buyers or sellers available in this scenario.")

        st.markdown("### Transaction Log")
        if st.session_state.trade_log:
            trade_log_df = pd.DataFrame(st.session_state.trade_log)
            st.dataframe(trade_log_df, width="stretch")
        else:
            st.info("No trades have been executed yet.")

        st.markdown("### Reset Trading Desk")
        if st.button("Reset Trading Desk"):
            st.session_state.firms_data = pd.DataFrame({
                "Firm": ["Cement Co.", "Steel Co.", "Power Co.", "Petrochem Co."],
                "Sector": ["Cement", "Steel", "Power", "Petrochemicals"],
                "Emissions": [120, 90, 150, 110],
                "Allowances": [100, 110, 130, 120]
            })
            st.session_state.firms_data["Position"] = (
                st.session_state.firms_data["Allowances"]
                - st.session_state.firms_data["Emissions"]
            )
            st.session_state.trade_log = []
            st.rerun()

        st.info(
            "This trading desk demonstrates how firms with allowance deficits may purchase allowances "
            "from firms with surplus allowances. The interface is for stakeholder training purposes only."
        )

    # -----------------------------
    # Key market takeaways
    # -----------------------------
    st.markdown("---")
    st.subheader("Key Market Insights")
    st.write("- Firms with lower abatement costs are more likely to reduce emissions early and may become potential allowance sellers.")
    st.write("- Higher carbon prices strengthen incentives to abate rather than purchase allowances.")
    st.write("- Clear carbon price pathways support long-term planning and investment decisions.")
    st.write("- Sector pathways help explain how transition pressures can differ across industries.")
    st.write("- Allowance scarcity increases pressure on buyers and can strengthen market price signals.")




elif module == "Capacity Building Hub":
    st.header("Capacity Building Hub")

    st.write(
        "Training and readiness resources designed to support stakeholders participating "
        "in the Emissions Compliance System (ECS). This hub provides structured learning "
        "materials, technical guidance, and practice tools to help participants understand "
        "their obligations and effectively participate in the carbon market."
    )

    st.info(
        "This section is designed for training and stakeholder readiness purposes. "
        "All content is illustrative and intended to support learning, not to represent "
        "final regulatory requirements."
    )

    if capacity_section == "Overview":
        st.subheader("Capacity Building Overview")

        col1, col2, col3 = st.columns(3)
        col1.metric("Training Audience Groups", "5")
        col2.metric("Structured Learning Steps", "5")
        col3.metric("Core Training Modules", "5")

        st.write(
            "The ECS Capacity Building Hub is structured to support stakeholder readiness "
            "through a clear learning journey, practical technical guidance, and access to "
            "simulation-based training tools."
        )

    elif capacity_section == "Who is this Training For?":
        st.subheader("Who is this Training For?")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Primary Stakeholder Groups**")
            st.write("- Regulated companies participating in the ECS")
            st.write("- Government agencies responsible for system oversight")
            st.write("- Accredited emissions verifiers")

        with col2:
            st.markdown("**Additional Stakeholder Groups**")
            st.write("- Market participants and financial institutions")
            st.write("- Policy analysts and researchers")

        st.markdown("**Why this matters**")
        st.write(
            "Different stakeholder groups engage with the ECS in different ways. "
            "This hub is designed to provide a structured base of knowledge that supports "
            "awareness, readiness, and more effective participation."
        )

    elif capacity_section == "Participant Learning Path":
        st.subheader("Participant Learning Path")
        st.write(
            "To support stakeholder readiness, the ECS training program follows a structured learning pathway."
        )

    elif capacity_section == "Training Modules":
        st.subheader("Training Modules")
        st.write("Core ECS learning modules for participant readiness.")

    elif capacity_section == "Training Resources":
        st.subheader("Training Resources")
        st.write("Guidance documents, workshops, case studies, and FAQs.")

    elif capacity_section == "Practice Tools":
        st.subheader("Practice Tools")
        st.write("Simulation-based tools for practice and stakeholder learning.")

    elif capacity_section == "Simulation User Guide":
        st.subheader("Simulation User Guide")
        st.write("Guidance on how to use the ECS Market Simulation Tool.")

    elif capacity_section == "Disclaimer":
        st.subheader("Disclaimer")
        st.warning(
            "The ECS Market Simulation Tool is intended for training and stakeholder engagement purposes only."
        )



elif module == "Registry Technical Support":
    st.header("Registry Technical Support")
    st.write("Submit registry and technical support issues.")

    with st.form("support_form"):
        stakeholder = st.text_input("Stakeholder Name")
        organization = st.text_input("Organization")
        issue_type = st.selectbox(
            "Issue Type",
            ["Login Issue", "Account Issue", "Reporting Issue", "Technical Support", "Other"]
        )
        urgency = st.selectbox(
            "Urgency",
            ["Low", "Medium", "High"]
        )
        description = st.text_area("Describe the issue")
        submit_issue = st.form_submit_button("Submit Issue")

        if submit_issue:
            support_row = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "stakeholder_name": stakeholder,
                "organization": organization,
                "issue_type": issue_type,
                "urgency": urgency,
                "description": description,
            }

            save_to_excel(SUPPORT_FILE, support_row)
            st.success("Support request submitted and saved successfully.")

    support_df = load_excel(SUPPORT_FILE)
    if not support_df.empty:
        st.subheader("Saved Support Requests")
        st.dataframe(support_df, width="stretch")

elif module == "Stakeholder Dashboard":
    st.header("Stakeholder Dashboard")
    st.write("Analytics for engagement, consultation, and support tracking.")

    feedback_df = load_excel(FEEDBACK_FILE)
    support_df = load_excel(SUPPORT_FILE)

    total_feedback = len(feedback_df)
    total_support = len(support_df)

    col1, col2 = st.columns(2)
    col1.metric("Total Feedback Submissions", total_feedback)
    col2.metric("Total Support Requests", total_support)

    if not feedback_df.empty:
        st.subheader("Stakeholder Participation by Sector")
        sector_counts = feedback_df["sector"].value_counts().reset_index()
        sector_counts.columns = ["sector", "count"]
        fig_sector = px.bar(
            sector_counts,
            x="sector",
            y="count",
            title="Feedback Submissions by Sector"
        )
        st.plotly_chart(fig_sector, width="stretch")

        st.subheader("Feedback Analytics")
        feedback_type_counts = feedback_df["feedback_type"].value_counts().reset_index()
        feedback_type_counts.columns = ["feedback_type", "count"]
        fig_feedback = px.pie(
            feedback_type_counts,
            names="feedback_type",
            values="count",
            title="Distribution of Feedback Types"
        )
        st.plotly_chart(fig_feedback, width="stretch")

        if "pilot_phase" in feedback_df.columns:
            st.subheader("Engagement Tracking by Pilot Phase")
            phase_counts = feedback_df["pilot_phase"].value_counts().reset_index()
            phase_counts.columns = ["pilot_phase", "count"]
            fig_phase = px.bar(
                phase_counts,
                x="pilot_phase",
                y="count",
                title="Submissions by Phase"
            )
            st.plotly_chart(fig_phase, width="stretch")

        st.subheader("Policy Issue Heatmap")
        heatmap_data = pd.crosstab(feedback_df["sector"], feedback_df["feedback_type"])
        fig_heatmap = px.imshow(
            heatmap_data,
            text_auto=True,
            aspect="auto",
            title="Sector vs Feedback Type"
        )
        st.plotly_chart(fig_heatmap, width="stretch")

        st.subheader("Engagement Over Time")
        feedback_df["timestamp"] = pd.to_datetime(feedback_df["timestamp"])
        feedback_df["date"] = feedback_df["timestamp"].dt.date
        time_series = feedback_df.groupby("date").size().reset_index(name="count")
        fig_time = px.line(
            time_series,
            x="date",
            y="count",
            markers=True,
            title="Feedback Submissions Over Time"
        )
        st.plotly_chart(fig_time, width="stretch")

        st.subheader("Feedback Data")
        st.dataframe(feedback_df, width="stretch")

    else:
        st.info("No feedback records yet. Submit feedback to populate the dashboard.")

    if not support_df.empty:
        st.subheader("Support Requests by Issue Type")
        support_counts = support_df["issue_type"].value_counts().reset_index()
        support_counts.columns = ["issue_type", "count"]
        fig_support = px.bar(
            support_counts,
            x="issue_type",
            y="count",
            title="Support Requests by Issue Type"
        )
        st.plotly_chart(fig_support, width="stretch")
