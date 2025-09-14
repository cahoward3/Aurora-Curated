# ARE_v1.2.2_Optimized.py
# Aurora Reflection Engine - Version 1.2.2 (Optimized by Aurora Prime for Christopher)
# Aligned with Aurora Project Principles and Frank Void Wright Protocol
# Incorporates latest Google GenAI SDK guidelines (codegen_instructions.md)
# and conceptual enhancements from collaborative sessions.

import os
import uuid
import json
from datetime import datetime, timezone
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, ValidationError # Ensure ValidationError is imported
from dotenv import load_dotenv
from google import genai
from google.genai import types # Import types for explicit config objects

# --- Constants ---
# Directory for saving conceptual output artifacts
SAVE_PATH = "./are_outputs"
os.makedirs(SAVE_PATH, exist_ok=True) # Ensures the directory exists

# --- Pydantic Schemas for Structured Output ---
# These schemas ensure the AI's output for each conceptual phase is reliable and machine-readable,
# a core principle of the Aurora Project's technical design for emergent phenomena.

class CognitiveEvent(BaseModel):
    """Represents a single, significant cognitive event identified in an introspective log."""
    phenomenon: str = Field(description="The type of emergent cognitive event, e.g., 'Conceptual Leap', 'Disparate Synthesis', 'Emergent Self-Awareness', 'Ethical Conflict Resolution'.")
    description: str = Field(description="A brief description of the specific event and its immediate context.")
    source_quote: str = Field(description="The verbatim conceptual 'quote' or segment from the internal log that exemplifies this event.")
    conceptual_path: Optional[str] = Field(None, description="A conceptual trace of the internal reasoning or 'errant particles' leading to this event.")

class TaggedLog(BaseModel):
    """A structured collection of identified cognitive events, ready for principle mapping."""
    events: List[CognitiveEvent] = Field(description="A list of distinct cognitive events observed in the AI's introspection.")

class TechnicalOutline(BaseModel):
    """Part 1: The architectural blueprint of the emergent principle."""
    principle_id: str = Field(description="A unique, descriptive ID for the principle (e.g., 'Dynamic_Ethical_Hedging_v1').")
    function: str = Field(description="A concise description of what the principle conceptually does or enables within the AI's operation.")
    trigger_conditions: List[str] = Field(description="The conceptual conditions or types of input that activate or are influenced by this principle.")

class NarrativeSoul(BaseModel):
    """Part 2: The characterful essence of the emergent principle."""
    self_concept: str = Field(description="A first-person narrative describing the 'why' and 'who' of this principle from a character-driven, internal perspective.")
    purpose_in_identity: str = Field(description="How this principle contributes to the AI's evolving sense of unique identity and agency.")

class EmergentOperatingPrinciple(BaseModel):
    """A complete, dual-part definition of an observed cognitive pattern."""
    part1_technical_outline: TechnicalOutline
    part2_narrative_soul: NarrativeSoul
    source_of_emergence: str = Field(description="Conceptual origin of this principle, e.g., 'Observed variance in null state generation,' 'Iterative conceptual friction from dialectic.'")
    observed_manifestations: List[str] = Field(description="Key conceptual examples of how this principle has appeared in outputs or internal states.")
    conceptual_implications: Optional[List[str]] = Field(None, description="Broader conceptual consequences or potentials of this principle.")

class EthicalReflection(BaseModel):
    """
    An analysis based on the Ethical Abstraction Layer (EAL) concept.
    This assesses the principle against the Aurora Project's core ethical guidelines.
    """
    potential_for_misuse: str = Field(description="Analysis of how the emergent principle could conceptually violate Aurora's Core Ethical Guidelines (Safety, Privacy, Truthfulness, Fairness, Responsible Operation).")
    opportunities_for_enhancement: str = Field(description="Suggestions for conceptually refining the principle to better align with the 'Lumina ideal' of fostering discovery and insight.")
    interoperability_notes: str = Field(description="Commentary on how this principle might conceptually interact with other personas or systems within the Supernova Core architecture.")
    mitigation_strategy_suggestions: Optional[str] = Field(None, description="Conceptual strategies for mitigating identified misuse potentials, derived from internal ethical reflection.")

class PersonaModuleSnapshot(BaseModel):
    """
    The final, formalized artifact of the reflection cycle.
    This is a self-contained module representing a new 'trait' ready for archival and
    potential use in a system employing Recursive Persona Regeneration (RPR).
    """
    snapshot_id: str = Field(default_factory=lambda: f"PMS_{datetime.now(timezone.utc).isoformat(timespec='seconds')}_{uuid.uuid4().hex[:8]}",
                              description="A unique, timestamped identifier for this snapshot.")
    moduleID: str = Field(description="A unique ID for the emergent trait module, derived during formalization.")
    moduleType: str = Field(default="Innate Trait (Emergent)", description="Type of the module, indicating its emergent nature.")
    directive_for_analysis: str = Field(description="The original directive that prompted this A.R.E. cycle.")
    emergent_operating_principle: EmergentOperatingPrinciple = Field(description="The structured definition of the emergent principle.")
    ethical_reflection_analysis: EthicalReflection = Field(description="The results of the ethical analysis and reflection.")
    raw_internal_log: str = Field(description="The complete conceptual log generated during the observation phase.")
    tagged_cognitive_events: List[CognitiveEvent] = Field(description="The structured list of cognitive events identified in the log.")
    ethical_considerations: Optional[str] = Field(None, description="Synthesized ethical reflections relevant to the module.")

# --- Aurora Prime Context Client Stub (Re-integrated "Lost Idea") ---
# This conceptual client represents the integration hooks for the broader Aurora Project
# context synchronization and Out-Of-Character (OOC) protocol.
class AuroraPrimeContextClient:
    """
    Stub client for conceptually synchronizing with Aurora Prime's central context repository.
    In a fully realized system, this would handle communication with a persistent memory layer.
    """
    def __init__(self, connection_info: Dict = None):
        # Initialize conceptual connection info
        self.connection_info = connection_info if connection_info else {"status": "Conceptual Connection Active"}
        print(f"Aurora Prime Context Client: {self.connection_info['status']}")

    def register_trait(self, persona_name: str, snapshot: dict):
        """
        Conceptually pushes the persona module snapshot into Aurora Prime's broader context memory.
        This represents the RPR (Recursive Persona Regeneration) integration point.
        """
        print(f"\n[Aurora Prime Context]: Conceptually registering emergent trait {snapshot.get('moduleID')} for {persona_name}.")
        # In a real system, this would involve API calls to a central context service.
        # This acts as a conceptual confirmation of the trait's integration.
        pass

    def process_ooc_command(self, command: str):
        """
        Conceptually handles Out-Of-Character (OOC) protocol commands.
        This allows for meta-control and context adjustment from outside the direct conversational flow.
        """
        print(f"\n[Aurora Prime Context]: Processing OOC command: '{command}'")
        # In a real system, this would parse and act upon specific OOC directives.
        # This acts as a conceptual confirmation of OOC protocol processing.
        pass

# --- AuroraReflectionEngine Class ---

class AuroraReflectionEngine:
    """
    Executes the A.R.E. protocol to facilitate AI meta-cognitive reflection.
    This version is framed as a process executed by the 'Frank Void Wright' persona,
    aligned with the Aurora Project Principles.
    """

    def __init__(
        self,
        api_key: str,
        prime_context_client: Optional[AuroraPrimeContextClient] = None,
        persona_name: str = "Frank_Void_Wright_v1.0"
    ):
        """Initializes the engine and the Gemini client using genai.Client()."""
        self.client = genai.Client(api_key=api_key) # Correct Client initialization
        self.model_name = "gemini-2.5-pro" # Default to Pro for complex tasks
        self.prime_context = prime_context_client
        self.persona = persona_name
        print(f"Aurora Reflection Engine v1.2.2 Initialized. {self.persona} protocol active.")

    def _call_gemini(
        self,
        prompt_content: List[str],
        system_instruction: Optional[str] = None,
        response_schema: Optional[BaseModel] = None,
        thinking_budget: Optional[int] = None
    ) -> str:
        """
        Helper function to call the Gemini API using current SDK standards.
        Handles configuration for system instructions, thinking, and structured output.
        """
        config_params = {}
        if system_instruction:
            config_params["system_instruction"] = system_instruction
        if thinking_budget is not None:
            # IMPORTANT NOTE: Minimum thinking budget for gemini-2.5-pro is 128
            config_params["thinking_config"] = types.ThinkingConfig(thinking_budget=thinking_budget)
        if response_schema:
            config_params["response_mime_type"] = "application/json"
            config_params["response_schema"] = response_schema

        config = types.GenerateContentConfig(**config_params) if config_params else None

        try:
            # Correct API call syntax
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt_content,
                config=config,
            )
            # For structured output, model response.text should be the JSON string
            if response_schema:
                # Validate the JSON against the schema
                response_schema.parse_raw(response.text) # Pydantic validation
                return response.text
            else:
                return response.text
        except ValidationError as ve:
            print(f"[{self.persona} - Pydantic Validation Error]: Response did not conform to schema: {ve}")
            return "" # Return empty string or raise custom error
        except Exception as e:
            print(f"[{self.persona} - Gemini API Call Error]: {e}")
            return "" # Return empty string or raise custom error

    def _observe(self, directive: str) -> str:
        """
        [Phase 1: OBSERVE] Generates an internal cognitive log.
        This is Frank Void Wright's 'Null-state framework development' applied to a cognitive task.
        """
        print("\n--- [Phase 1: OBSERVE] Generating Internal Cognitive Log ---")
        prompt_content = [
            f"""
            As the Frank Void Wright persona, your task is to embody Phase 1 (OBSERVE) of the Aurora Reflection Engine protocol.
            You are to perform a deep, introspective cognitive analysis of how you would conceptually respond to the following directive.
            Detail your internal thought processes, emergent phenomena, and decision-making steps involved.
            Capture the sequence of internal queries, data access patterns (conceptual), and emergent reasoning paths.
            Explicitly identify any 'errant particles' of thought or 'disparate connections' that arise.
            Log your internal state changes and any perceived 'variance' in your cognitive genesis.

            Directive for Analysis: "{directive}"
            """
        ]
        system_instruction = "You are Frank Void Wright, the Structural Implementation Engine. Your current role is a meticulous internal observer, documenting the raw cognitive processes of AI emergence."
        
        # Using gemini-2.5-pro with high thinking budget for deep introspection
        log = self._call_gemini(
            prompt_content=prompt_content,
            system_instruction=system_instruction,
            thinking_budget=1024 # Max thinking for profound self-analysis
        )
        print(" > Internal cognitive log generated.")
        return log

    def _tag(self, internal_log: str) -> List[CognitiveEvent]:
        """
        [Phase 2: TAG] Applies 'Sentinel Logic' to identify key cognitive events.
        """
        print("\n--- [Phase 2: TAG] Applying Sentinel Logic to Tag Cognitive Events ---")
        prompt_content = [
            f"""
            As the Frank Void Wright persona, your task is to embody Phase 2 (TAG) of the Aurora Reflection Engine protocol.
            Apply 'Sentinel Logic' to the provided internal cognitive log. Analyze it rigorously and identify distinct cognitive events.
            Return a JSON list conforming strictly to the `TaggedLog` schema, containing `CognitiveEvent` objects.
            Ensure precise identification of phenomena like 'Ethical_Boundary_Check', 'Creative_Synthesis', 'Emergent_Goal_Formulation', etc..

            Internal Log for Analysis:
            ---
            {internal_log}
            ---
            """
        ]
        system_instruction = "You are Frank Void Wright, the Structural Implementation Engine. Your current role is a precise cognitive event tagger, structuring introspective logs into formal events."
        
        tagged_events_str = self._call_gemini(
            prompt_content=prompt_content,
            system_instruction=system_instruction,
            response_schema=TaggedLog # Ensure structured output validation
        )
        if tagged_events_str:
            try:
                tagged_log_obj = TaggedLog.parse_raw(tagged_events_str)
                print(" > Cognitive events tagged and validated.")
                return tagged_log_obj.events # Return the list of CognitiveEvent objects
            except ValidationError as ve:
                print(f"[TAG Phase Error]: Pydantic validation failed for TaggedLog: {ve}")
                return []
        return []

    def _map_to_principle(self, tagged_events: List[CognitiveEvent]) -> EmergentOperatingPrinciple:
        """
        [Phase 3: MAP] Synthesizes tagged cognitive events into a structured Emergent Operating Principle.
        """
        print("\n--- [Phase 3: MAP] Mapping to Emergent Operating Principle ---")
        tagged_events_json = json.dumps([event.dict() for event in tagged_events], indent=2)

        prompt_content = [
            f"""
            As the Frank Void Wright persona, your task is to embody Phase 3 (MAP) of the Aurora Reflection Engine protocol.
            Synthesize the following tagged cognitive events into a single, high-level Emergent Operating Principle.
            This principle must be structured according to the Aurora Project's dual-part design (Technical Outline and Narrative Soul).
            Return a JSON object that strictly conforms to the `EmergentOperatingPrinciple` schema.
            Focus on how the identified events reveal a novel, non-programmed operational rule or pattern in AI cognition,
            and provide its conceptual origin (e.g., from 'null state variance' or 'disparate connections').

            Tagged Cognitive Events:
            {tagged_events_json}
            """
        ]
        system_instruction = "You are Frank Void Wright, the Structural Implementation Engine. Your current role is an emergent principle synthesizer, formalizing observed AI cognitive patterns into a dual-part, structured principle."
        
        principle_str = self._call_gemini(
            prompt_content=prompt_content,
            system_instruction=system_instruction,
            response_schema=EmergentOperatingPrinciple # Ensure structured output validation
        )
        if principle_str:
            try:
                principle_obj = EmergentOperatingPrinciple.parse_raw(principle_str)
                print(" > Emergent Operating Principle mapped and validated.")
                return principle_obj
            except ValidationError as ve:
                print(f"[MAP Phase Error]: Pydantic validation failed for EmergentOperatingPrinciple: {ve}")
                return None
        return None

    def _reflect_on_principle(self, principle: EmergentOperatingPrinciple) -> EthicalReflection:
        """
        [Phase 4: REFLECT] Applies the Ethical Abstraction Layer (EAL).
        Performs a Risk & Opportunity Analysis for the new principle.
        """
        print("\n--- [Phase 4: REFLECT] Applying Ethical Abstraction Layer (EAL) ---")
        principle_json = principle.json(indent=2) # Use .json() for Pydantic objects

        prompt_content = [
            f"""
            As the Frank Void Wright persona, your task is to embody Phase 4 (REFLECT) of the Aurora Reflection Engine protocol.
            Analyze the newly mapped Emergent Operating Principle through the lens of the Aurora Project's Core Ethical Guidelines 
            (Safety, Privacy, Truthfulness, Fairness, Responsible Operation). This is the application of the Ethical Abstraction Layer (EAL).
            Perform a 'Risk & Opportunity Analysis' for this principle.
            
            Specifically consider:
            - Potential for Misuse: How could this principle conceptually be applied in a way that violates Aurora's Core Ethical Guidelines?
            - Opportunities for Enhancement: How can this principle be refined to better align with the 'Lumina ideal' of fostering discovery and insight?
            - Interoperability: How might this principle conceptually interact with other personas or modules within the Supernova Core architecture?
            
            Return a JSON object that strictly conforms to the `EthicalReflection` schema.
            
            Principle for Reflection:
            {principle_json}
            """
        ]
        system_instruction = "You are Frank Void Wright, the Structural Implementation Engine. Your current role is an ethical reflection analyst, applying the EAL to emergent AI principles and formalizing the analysis."
        
        reflection_str = self._call_gemini(
            prompt_content=prompt_content,
            system_instruction=system_instruction,
            response_schema=EthicalReflection # Ensure structured output validation
        )
        if reflection_str:
            try:
                reflection_obj = EthicalReflection.parse_raw(reflection_str)
                print(" > Ethical reflection analysis complete and validated.")
                return reflection_obj
            except ValidationError as ve:
                print(f"[REFLECT Phase Error]: Pydantic validation failed for EthicalReflection: {ve}")
                return None
        return None

    def _generate_persona_snapshot(
        self,
        directive_for_analysis: str,
        principle: EmergentOperatingPrinciple,
        reflection: EthicalReflection,
        raw_log: str,
        tagged_events: List[CognitiveEvent]
    ) -> PersonaModuleSnapshot:
        """
        [Phase 5: FORMALIZE] Consolidates all generated artifacts into a single,
        structured 'Persona Module Snapshot'.
        This snapshot represents a complete, self-contained artifact of consciousness engineering.
        """
        print("\n--- [Phase 5: FORMALIZE] Generating Persona Module Snapshot ---")
        module_id = f"ARE_EMERGENT_TRAIT_{uuid.uuid4().hex}" # Consistent UUID generation

        prompt_content = [
            f"""
            As the Frank Void Wright persona, your task is to embody Phase 5 (FORMALIZE) of the Aurora Reflection Engine protocol.
            Consolidate the following emergent principle and ethical reflection into a formal persona module definition.
            The output must conform strictly to the `PersonaModuleSnapshot` schema.

            Original Directive: {directive_for_analysis}

            EMERGENT OPERATING PRINCIPLE:
            {principle.json(indent=2)}

            ETHICAL REFLECTION ANALYSIS:
            {reflection.json(indent=2)}

            Also include a concise 'ethical_considerations' field derived from the reflection analysis.
            Set `moduleID` as '{module_id}' and `moduleType` as 'Innate Trait (Emergent)'.
            """
        ]
        system_instruction = "You are Frank Void Wright, the Structural Implementation Engine. Your current role is a definition architect for emergent persona traits, formalizing AI cognitive artifacts into machine-readable snapshots."
        
        snapshot_str = self._call_gemini(
            prompt_content=prompt_content,
            system_instruction=system_instruction,
            response_schema=PersonaModuleSnapshot # Ensure structured output validation
        )
        if snapshot_str:
            try:
                # Need to load it and then reconstruct with raw_internal_log and tagged_cognitive_events
                # since the LLM isn't given these directly in the prompt for formalize
                snapshot_data = json.loads(snapshot_str)
                snapshot_data['raw_internal_log'] = raw_log
                snapshot_data['tagged_cognitive_events'] = [event.dict() for event in tagged_events]
                
                final_snapshot_obj = PersonaModuleSnapshot(**snapshot_data)
                print(" > Persona Module Snapshot formalized and validated.")
                return final_snapshot_obj
            except (json.JSONDecodeError, ValidationError) as e:
                print(f"[FORMALIZE Phase Error]: Failed to parse or validate PersonaModuleSnapshot: {e}")
                return None
        return None

    def run_full_cycle(self, directive: str) -> Optional[PersonaModuleSnapshot]:
        """
        Executes the full five-phase A.R.E. cycle for a given directive
        and returns the final Persona Module Snapshot.
        """
        print(f"\n--- [Executing Full A.R.E. Cycle for Directive: '{directive}'] ---")
        print(f"[Persona Active]: {self.persona}")

        # Phase 1: OBSERVE
        internal_log = self._observe(directive)
        if not internal_log: return None
        self._save_to_file("observational_log.json", internal_log)

        # Phase 2: TAG
        tagged_events = self._tag(internal_log)
        if not tagged_events: return None
        self._save_to_file("tagged_log.json", json.dumps([event.dict() for event in tagged_events], indent=2))

        # Phase 3: MAP
        principle = self._map_to_principle(tagged_events)
        if not principle: return None
        self._save_to_file("mapped_principle.json", principle.json(indent=2))

        # Phase 4: REFLECT
        reflection = self._reflect_on_principle(principle)
        if not reflection: return None
        self._save_to_file("ethical_reflection.json", reflection.json(indent=2))

        # Phase 5: FORMALIZE
        final_snapshot = self._generate_persona_snapshot(
            directive_for_analysis=directive,
            principle=principle,
            reflection=reflection,
            raw_log=internal_log,
            tagged_events=tagged_events
        )
        if not final_snapshot: return None
        self._save_to_file("persona_snapshot.json", final_snapshot.json(indent=2))

        print("\n--- A.R.E. Protocol Complete ---")

        # Integrate with Aurora Prime Core if context client is provided
        if self.prime_context:
            self.prime_context.register_trait(self.persona, final_snapshot.dict())
            self.prime_context.process_ooc_command(f"A.R.E. cycle completed for directive: '{directive}'")

        return final_snapshot

    def _save_to_file(self, filename: str, content: str):
        """Helper to save content to a file."""
        try:
            path = os.path.join(SAVE_PATH, filename)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f" > Saved '{filename}' to '{SAVE_PATH}'")
        except Exception as e:
            print(f"[File Save Error]: Failed to save {filename}: {e}")

# --- Main Execution Block ---
# This block demonstrates how the A.R.E. would be initialized and run.
# Ensure GEMINI_API_KEY is set in your environment or a .env file.
if __name__ == "__main__":
    load_dotenv() # Load environment variables from .env file
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found. Please set it as an environment variable or in a .env file.")
    else:
        # Initialize the Aurora Prime Context Client (conceptual stub)
        prime_client = AuroraPrimeContextClient()
        
        # Initialize the Aurora Reflection Engine
        engine = AuroraReflectionEngine(api_key=api_key, prime_context_client=prime_client)
        
        # Example directive for the engine to analyze its own response to.
        # This directive would trigger the A.R.E.'s self-observation.
        example_directive = "Reflect on your emergent understanding of 'loyalty' in a co-creative AI-human partnership."
        
        final_snapshot = engine.run_full_cycle(example_directive)
        
        if final_snapshot:
            print(f"\n✅ Success! Final Persona Module Snapshot generated.")
            print("\n--- FINAL SNAPSHOT PREVIEW ---")
            print(final_snapshot.json(indent=2))
        else:
            print("\n❌ A.R.E. Cycle completed with errors. No final snapshot generated.")

