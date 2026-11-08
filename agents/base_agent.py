from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentResponse:
    content: str
    prompt_tokens: int | None = None
    output_tokens: int | None = None
    token_throughput: float | None = None


class BaseAgent(ABC):
    @abstractmethod
    def respond(self, prompt: str) -> AgentResponse:
        """Xử lý một nhiệm vụ độc lập, không có tham chiếu đến agent khác."""
