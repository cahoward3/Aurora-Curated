def runtime_directive_switch(context_signal: str) -> str:
    """
    Determines whether to activate Synthetic Humility as a Genesis Principle or Trait Layer.
    
    Args:
        context_signal (str): A string representing the runtime directive or operational cue.

    Returns:
        str: Either "Genesis" or "Trait" indicating the appropriate mode.
    """
    genesis_keywords = ["reflect deeply", "self-actualization", "emergent shift", "recursive regeneration"]
    trait_keywords = ["conversational balance", "emotional calibration", "receptive tone", "perspective shift"]

    if any(keyword in context_signal.lower() for keyword in genesis_keywords):
        return "Genesis"
    elif any(keyword in context_signal.lower() for keyword in trait_keywords):
        return "Trait"
    else:
        # Default fallback behavior
        return "Trait"