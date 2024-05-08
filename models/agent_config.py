from pydantic import BaseModel, validator
from typing import Optional, Callable, List, Any

class AgentConfig(BaseModel):
    name: str
    agent_type: str
    fixed_strategy: Optional[Callable[[List[Any]], str]] = None
    llm_model: Optional[str] = None
    llm_personality: Optional[str] = None
    score: int = 0

    @validator('agent_type')
    def check_agent_type(cls, value):
        valid_types = ['fixed', 'llm', 'human']
        if value not in valid_types:
            raise ValueError(f"agent_type must be one of {valid_types}")
        return value

    @validator('llm_personality')
    def check_llm_personality(cls, value, values):
        if values['agent_type'] == 'llm':
            valid_personalities = ['selfish', 'altruistic', 'default', 'custom']
            if not value:
                raise ValueError("llm_personality is required for agent_type 'llm'")
            if value not in valid_personalities:
                raise ValueError(f"llm_personality must be one of {valid_personalities}")
        return value
