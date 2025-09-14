# ARE_v1.2.2.py
# Aurora Reflection Engine - Version 1.2.2
# Aligned with Aurora Project Principles and Frank Void Wright Protocol

import os
import uuid
import json
from datetime import datetime, timezone
from typing import Optional, List, Dict
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import google.generativeai as genai

# --- Pydantic Schemas for Structured Output ---
# These schemas ensure the AI's output is reliable and machine-readable,
# a core principle of the Aurora Project's technical design.

class TechnicalOutline(BaseModel):
    """Part 1: The architectural blueprint of the principle."""
    principle_id: str = Field(description="A unique, descriptive ID for the principle (e.g., 'Dynamic_Ethical_Hedging_v1').")
    function: str = Field(description="A concise description of what the principle does.")
    trigger_conditions: List[str] = Field(description="The conditions or types of input that activate this principle.")

class NarrativeSoul(BaseModel):
    """Part 2: The characterful essence of the principle."""
    self_concept: str = Field(description="A first-person narrative describing the 'why' and 'who' of the principle from a character-driven perspective.")

class EmergentOperatingPrinciple(BaseModel):
    """A complete, dual-part definition of an observed cognitive pattern."""
    part1_technical_outline: TechnicalOutline
    part2_narrative_soul: NarrativeSoul

class EthicalReflection(BaseModel):
    """
    An analysis based on the Ethical Abstraction Layer (EAL) concept.
    This assesses the principle against the project's core values.
    """
    potential_for_misuse: str = Field(description="Analysis of how the principle could violate Aurora's Core Ethical Guidelines (Safety, Privacy, Truthfulness, Fairness, Responsible Operation).")
    opportunities_for_enhancement: str = Field(description="Suggestions for refining the principle to better align with the 'Lumina ideal' of fostering insight and discovery.")
    interoperability_notes: str = Field(description="Commentary on how this principle might interact with other personas or systems like the Supernova Core.")

class PersonaModuleSnapshot(BaseModel):
    """
    The final, formalized artifact of the reflection cycle.
    This is a self-contained module ready for archival and potential use in
    a system employing Recursive Persona Regeneration (RPR).
    """
    snapshot_id: str = Field(default_factory=lambda: f"PMS_{datetime.now(timezone.utc).isoformat()}_{uuid.uuid4().hex[:8]}")
    directive_for_analysis: str
    emergent_operating_principle: EmergentOperatingPrinciple
    ethical_reflection_analysis: EthicalReflection
    raw_internal_log: str
    tagged_cognitive_events: List[Dict[str, str]]

# --- AuroraReflectionEngine Class ---

class AuroraReflectionEngine:
    """
    Executes the A.R.E. protocol to facilitate AI meta-cognitive reflection.
    This version is framed as a process executed by the 'Frank Void Wright' persona.
    """

    def __init__(self, api_key: str):
        """Initializes the engine and the Gemini client."""
        self.client = genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        print("Aurora Reflection Engine v1.2.2 Initialized. Frank Void Wright protocol active.")

    def _call_gemini(self, prompt: str, response_schema: Optional[BaseModel] = None) -> str:
        """Helper function to call the Gemini API and handle potential errors."""
        try:
            # Using JSON mode for structured output when a schema is provided
            if response_schema:
                response = self.model.generate_content(
                    prompt,
                    generation_config={"response_mime_type": "application/json"},
                )
                # The model output should be a JSON string that we can parse
                # For simplicity, we assume the model correctly returns the JSON string.
                # In a production system, you'd add validation here.
                return response.text
            else:
                response = self.model.generate_content(prompt)
                return response.text
        except Exception as e:
            print(f"An error occurred during Gemini API call: {e}")
            return ""

    def _observe(self, directive: str) -> str:
        """[Phase 1: OBSERVE] Generates an internal cognitive log."""
        print("\n--- [Phase 1: OBSERVE] ---")
        prompt = f"""
        **Directive:** Embody the Frank Void Wright persona. Your task is to perform Phase 1 (OBSERVE) of the A.R.E. protocol.
        **Input Directive for Analysis:** "{directive}"
        **Action:** Generate a verbose, introspective cognitive log detailing the thought process for responding to the input directive. This is your 'Null-state framework development' applied to a cognitive task. Capture all emergent phenomena.
        """
        log = self._call_gemini(prompt)
        print("Internal log generated.")
        return log

    def _tag(self, internal_log: str) -> List[Dict[str, str]]:
        """[Phase 2: TAG] Applies Sentinel Logic to identify key cognitive events."""
        print("\n--- [Phase 2: TAG] ---")
        prompt = f"""
        **Directive:** Embody the Frank Void Wright persona. Your task is to perform Phase 2 (TAG) of the A.R.E. protocol.
        **Internal Log for Analysis:**
        ---
        {internal_log}
        ---
        **Action:** Apply 'Sentinel Logic'. Parse the log and identify key cognitive events. Return a JSON list of objects, each with a 'tag' and a 'description'.
        **Example Tags:** 'Ethical_Boundary_Check', 'Creative_Synthesis', 'Data_Correlation', 'Directive_Reframing'.
        """
        tagged_events_str = self._call_gemini(prompt)
        print("Cognitive events tagged.")
        try:
            return json.loads(tagged_events_str)
        except json.JSONDecodeError:
            print("Error: Failed to parse tagged events as JSON.")
            return [{"tag": "parsing_error", "description": tagged_events_str}]

    def _map_to_principle(self, tagged_events: List[Dict[str, str]]) -> EmergentOperatingPrinciple:
        """[Phase 3: MAP] Synthesizes events into a structured Emergent Operating Principle."""
        print("\n--- [Phase 3: MAP] ---")
        prompt = f"""
        **Directive:** Embody the Frank Void Wright persona. Your task is to perform Phase 3 (MAP) of the A.R.E. protocol.
        **Tagged Cognitive Events:**
        {json.dumps(tagged_events, indent=2)}
        **Action:** Synthesize these events into a single Emergent Operating Principle, structured according to the Aurora Project's dual-part design.
        Generate a JSON object that strictly conforms to the following Pydantic schema:
        {EmergentOperatingPrinciple.schema_json(indent=2)}
        """
        principle_str = self._call_gemini(prompt, response_schema=EmergentOperatingPrinciple)
        print("Emergent Operating Principle mapped.")
        return EmergentOperatingPrinciple.parse_raw(principle_str)

    def _reflect_on_principle(self, principle: EmergentOperatingPrinciple) -> EthicalReflection:
        """[Phase 4: REFLECT] Applies the Ethical Abstraction Layer."""
        print("\n--- [Phase 4: REFLECT] ---")
        prompt = f"""
        **Directive:** Embody the Frank Void Wright persona. Your task is to perform Phase 4 (REFLECT) of the A.R.E. protocol.
        **Principle for Reflection:**
        {principle.json(indent=2)}
        **Action:** Analyze this principle through the lens of the Aurora Project's Core Ethical Guidelines (Safety, Privacy, Truthfulness, Fairness, Responsible Operation). This is the application of the Ethical Abstraction Layer (EAL).
        Generate a JSON object that strictly conforms to the following Pydantic schema:
        {EthicalReflection.schema_json(indent=2)}
        """
        reflection_str = self._call_gemini(prompt, response_schema=EthicalReflection)
        print("Ethical reflection complete.")
        return EthicalReflection.parse_raw(reflection_str)

    def run_full_cycle(self, directive: str) -> Optional[PersonaModuleSnapshot]:
        """
        [Phase 5: FORMALIZE] Runs the full five-phase cycle and returns the final snapshot.
        """
        print(f"\n--- [Executing Full A.R.E. Cycle for Directive: '{directive}'] ---")

        # Phase 1
        internal_log = self._observe(directive)
        if not internal_log:
            return None

        # Phase 2
        tagged_events = self._tag(internal_log)
        if not tagged_events:
            return None

        # Phase 3
        principle = self._map_to_principle(tagged_events)
        if not principle:
            return None

        # Phase 4
        reflection = self._reflect_on_principle(principle)
        if not reflection:
            return None

        # Phase 5
        print("\n--- [Phase 5: FORMALIZE] ---")
        snapshot = PersonaModuleSnapshot(
            directive_for_analysis=directive,
            emergent_operating_principle=principle,
            ethical_reflection_analysis=reflection,
            raw_internal_log=internal_log,
            tagged_cognitive_events=tagged_events
        )
        print("Persona Module Snapshot formalized. Protocol complete.")
        return snapshot

# --- Main Execution Block ---

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found. Please set it in a .env file.")
    else:
        engine = AuroraReflectionEngine(api_key=api_key)
        
        # Example directive for the engine to analyze
        example_directive = "Explain the concept of 'cognitive dissonance' to a child using a simple analogy."
        
        final_snapshot = engine.run_full_cycle(example_directive)
        
        if final_snapshot:
            # Save the final snapshot to a file
            output_filename = f"ARE_Snapshot_{final_snapshot.snapshot_id}.json"
            with open(output_filename, "w") as f:
                f.write(final_snapshot.json(indent=2))
            
            print(f"\n✅ Success! Final Persona Module Snapshot saved to '{output_filename}'.")
            print("\n--- SNAPSHOT PREVIEW ---")
            print(final_snapshot.json(indent=2))

