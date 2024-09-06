from abc import ABC, abstractmethod
from typing import Dict, List


class IResourceManager(ABC):
    @abstractmethod
    def get_resource_amount(self, resource: str) -> int:
        pass

    @abstractmethod
    def remove_resource(self, resource: str, amount: int) -> None:
        pass

    @abstractmethod
    def add_resource(self, resource: str, amount: int) -> None:
        pass


class IKnowledgeGraph(ABC):
    @abstractmethod
    def get_recipes(self) -> List[Dict[str, Dict[str, int]]]:
        pass
