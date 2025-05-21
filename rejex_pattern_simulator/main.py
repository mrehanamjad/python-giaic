import streamlit as st
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from graphviz import Source

# ---------- Utility Functions ----------

def build_nfa_from_regex(regex: str) -> NFA:
    return NFA.from_regex(regex)

def convert_nfa_to_dfa(nfa: NFA) -> DFA:
    return DFA.from_nfa(nfa)

def simulate_dfa(dfa: DFA, test_str: str) -> bool:
    return dfa.accepts_input(test_str)

def get_dfa_graphviz(dfa: DFA) -> str:
    """
    Generate Graphviz DOT source manually from DFA transitions
    """
    dot = 'digraph DFA {\n'
    dot += '    rankdir=LR;\n'
    dot += '    node [shape=doublecircle];\n'

    # Final states
    for state in dfa.final_states:
        dot += f'    "{state}";\n'

    dot += '    node [shape=circle];\n'

    # Transitions
    for from_state, paths in dfa.transitions.items():
        for symbol, to_state in paths.items():
            dot += f'    "{from_state}" -> "{to_state}" [label="{symbol}"];\n'

    # Start state arrow
    dot += f'    "" -> "{dfa.initial_state}";\n'

    dot += '}'
    return dot

# ---------- Streamlit UI ----------

st.set_page_config(page_title="Regex Pattern Simulator", layout="centered")
st.title("🔍 Regex Pattern Simulator using Automata Theory")

# Input regex and test string
regex = st.text_input("Enter a regular expression (e.g., a*b|ab):", value="a*b")
test_str = st.text_input("Enter a string to test:", value="aaab")

# Run simulation
if st.button("Run Simulation"):
    if regex and test_str:
        try:
            # Build NFA and DFA
            nfa = build_nfa_from_regex(regex)
            dfa = convert_nfa_to_dfa(nfa)
            accepted = simulate_dfa(dfa, test_str)

            # Result
            st.success("✅ String is ACCEPTED by the regex!" if accepted else "❌ String is REJECTED.")

            # Visualize DFA
            st.subheader("DFA Transition Diagram")
            graph_source = get_dfa_graphviz(dfa)
            st.graphviz_chart(graph_source)

            # Show DFA table
            st.subheader("DFA Transition Table")
            st.json(dfa.transitions)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both a regular expression and a string to test.")
