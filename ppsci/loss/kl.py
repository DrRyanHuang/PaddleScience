# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import Dict
from typing import Optional
from typing import Union

import paddle.nn.functional as F
from typing_extensions import Literal

import paddle
from ppsci.loss import base


class KLLoss01(base.Loss):
    r"""Class for KL loss in vae
    """

    # def __init__(
    #     self,
    #     reduction: Literal["mean", "sum"] = "mean",
    #     weight: Optional[Union[float, Dict[str, float]]] = None,
    # ):
    #     if reduction not in ["mean", "sum"]:
    #         raise ValueError(
    #             f"reduction should be 'mean' or 'sum', but got {reduction}"
    #         )
    #     super().__init__(reduction, weight)

    def __init__(self):
        super().__init__(None, None)

    def forward(self, mu, log_sigma):
        # 计算mu，log_sigma与 N(0,1)分布的差距
        base = paddle.exp(2. * log_sigma) + paddle.pow(mu, 2) - 1. - 2. * log_sigma
        loss = 0.5 * paddle.sum(base) / mu.shape[0]
        return loss