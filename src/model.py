"""
Feed forward Neural Network model.
Gives propability of matching to intent/ context to be used on answering.
See description in: https://www.cs.toronto.edu/~lczhang/360/lec/w03/nn.html
"""

from typing import Optional

import torch
import torch.nn as nn
from torch import Tensor


class Neural_Model(nn.Module):
    def __init__(
        self, input_size: int, hidden_size: int, num_classes: int
    ) -> None:
        super(Neural_Model, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x: Tensor) -> Optional[Tensor]:
        """
        Method is called when neural network used to make a prediction.

        Args:
            x (Tensor): input tensor

        Returns:
            Optional[Tensor]: output tensor
        """
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # Softmax and actuation will be made in train.py.
        return out
