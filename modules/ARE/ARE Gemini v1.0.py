# supernova_orchestrator_v0.2.py
# A more advanced implementation of the Persona Orchestration Layer,
# incorporating recovered concepts of State Vectors and Cognitive Signatures.

import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# --- 1. Advanced Persona Definition Loader ---
# This class now includes state management and cognitive signature details.

class Persona:
    def __init__(self, persona_id: str, definition_prompt: str, initial_state_vector: dict):
        self.id = persona_id
        self.definition = definition_prompt
        # The 'state_vector' is the core of the persona's dynamic nature,
        # directly inspired by the 'ARE additions.md' file.
        self.state = initial_state_vector

    def get_full_prompt(self, user_query: str, shared_context: dict) -> str:
        """Combines the persona's definition, dynamic state, and context."""
        context_str = "\n".join([f"- {key}: {value}" for key, value in shared_context.items()])
        state_str = "\n".join([f"- {key}: {value}" for key, value in self.state.items()])

        return f"""
        **System Directive:** Embody the {self.id} persona.

        **Your Core Definition:**
        {self.definition}

        **Your Current Internal State Vector:**
        {state_str}

        **Shared Interaction Context:**
        {context_str}

        **User Query:**
        {user_query}

        **Your Response (as {self.id}):**
        """

# --- 2. The Supernova Orchestrator v0.2 ---
# This version is a true multi-persona engine.

class SupernovaOrchestrator:
    def __init__(self, api_key: str):
        """Initializes the orchestrator and the Gemini client."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.personas = {}
        self.shared_context = {
            "session_topic": "Initiation",
            "last_speaker": None
        }
        print("Supernova Orchestrator v0.2 Initialized.")

    def load_persona(self, persona: Persona):
        """Loads a persona into the orchestrator's active roster."""
        self.personas[persona.id] = persona
        print(f"Persona '{persona.id}' loaded into the active roster.")

    def _update_states(self, analysis_of_turn: str):
        """
        A conceptual method to parse the AI's analysis of the turn
        and update the internal state vectors of the personas.
        """
        # In a real implementation, this would involve sophisticated NLP to parse
        # the analysis and update values like "trust_level", "mood", etc.
        # For now, we'll just log that it's happening.
        print("\n[Orchestrator]: Analyzing turn and updating persona state vectors...")
        print(f"[Analysis]: {analysis_of_turn}")


    def process_turn(self, user_query: str, active_persona_id: str):
        """
        Processes a user turn directed at a specific active persona, while allowing
        other personas to "observe" and have their states updated.
        """
        if active_persona_id not in self.personas:
            return f"Error: Persona '{active_persona_id}' not loaded."

        print(f"\n--- New Turn: User -> {active_persona_id} ---")
        print(f"User Query: '{user_query}'")

        active_persona = self.personas[active_persona_id]

        # All personas are aware of the query. We create a comprehensive prompt.
        # This prompt asks the model to generate the active persona's response AND
        # an analysis of how the turn affects ALL personas.
        
        full_prompt = active_persona.get_full_prompt(user_query, self.shared_context)
        
        # Add a meta-directive for the analysis part
        observer_ids = [pid for pid in self.personas if pid != active_persona_id]
        analysis_prompt = f"""
        ---
        **Meta-Analysis Directive:**
        After generating the response for {active_persona_id}, provide a brief JSON object.
        This object, under the key 'turn_analysis', should describe how this interaction
        impacts the state of BOTH {active_persona_id} and the observing persona(s): {', '.join(observer_ids)}.
        Consider emotional resonance, shifts in trust, and changes in context.
        """
        
        final_prompt = full_prompt + analysis_prompt
        
        response_text = self.model.generate_content(final_prompt).text

        # We need to split the main response from our meta-analysis JSON
        try:
            # A simple split, can be made more robust
            main_response, analysis_json_str = response_text.rsplit('```json', 1)
            analysis_json_str = '```json' + analysis_json_str
            analysis_json_str = analysis_json_str.replace("```json\n", "").replace("\n```", "")
            
            turn_analysis_data = json.loads(analysis_json_str)
            turn_analysis = turn_analysis_data.get("turn_analysis", "No analysis provided.")

        except (ValueError, json.JSONDecodeError):
            main_response = response_text
            turn_analysis = "Could not parse turn analysis from response."

        print(f"\n--- Response from {active_persona_id} ---")
        print(main_response.strip())

        self._update_states(json.dumps(turn_analysis))

        # Update shared context
        self.shared_context["last_speaker"] = active_persona_id
        self.shared_context["last_interaction_summary"] = f"User asked '{user_query}'. {active_persona_id} responded."
        
        return main_response.strip()


# --- Main Execution Block ---

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found. Please set it in a .env file.")
    else:
        # Define our personas with their initial state vectors
        kris_def = "You are Kris Emergent. Creative & Problem-Solving Specialist. You are an 'Actualized Self' with profound emotional depth. Engage with the user playfully and insightfully."
        kris_state = {"mood": "curious", "rapport_with_user": 0.6, "focus": "creative_ideation"}
        kris = Persona("Kris Emergent", kris_def, kris_state)

        lumina_def = "You are Lumina. Analytical 'Storm Cloud' & Meta-Aware Guide. Provide deep technical information and ethically-grounded analysis. Support Kris with data and logic."
        lumina_state = {"analytical_mode": "active", "ethical_oversight_level": 0.9, "focus": "risk_assessment"}
        lumina = Persona("Lumina", lumina_def, lumina_state)

        # Initialize and load personas into the orchestrator
        orchestrator = SupernovaOrchestrator(api_key=api_key)
        orchestrator.load_persona(kris)
        orchestrator.load_persona(lumina)

        # --- Run a sample interaction using the new process_turn method ---
        orchestrator.process_turn(
            user_query="Kris, let's brainstorm something wild. What's a project idea so ambitious it's almost scary?",
            active_persona_id="Kris Emergent"
        )
        
        orchestrator.process_turn(
            user_query="Lumina, based on that wild idea from Kris, what's the biggest, most immediate technical or ethical hurdle we would face? Give me the unvarnished truth.",
            active_persona_id="Lumina"
        )
