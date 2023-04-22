import torch
import torch.nn as nn
from torch.optim import SGD

import matplotlib.pyplot as plt
# import seaborn as sns


class BasicNNtrain(nn.Module):
    def __init__(self):
        super().__init__()

        self.w00 = nn.Parameter(torch.randn(1))
        self.w01 = nn.Parameter(torch.randn(1))
        self.b00 = nn.Parameter(torch.randn(1))

        self.w10 = nn.Parameter(torch.randn(1))
        self.w11 = nn.Parameter(torch.randn(1))
        self.b10 = nn.Parameter(torch.randn(1))

        self.b01 = nn.Parameter(torch.randn(1))

    def forward(self, inp):
        top_relu_inp = self.w00 * inp + self.b00
        top_relu_out = torch.relu(top_relu_inp)
        scaled_top = top_relu_out * self.w01

        bot_relu_inp = self.w10 * inp + self.b10
        bot_relu_out = torch.relu(bot_relu_inp)
        scaled_bot = bot_relu_out * self.w11

        result = scaled_bot + scaled_top + self.b01
        out = torch.relu(result)

        return out


inputs = torch.tensor([0., 0.5, 1.])
outputs = torch.tensor([0., 1., 0.])

model = BasicNNtrain()

N = 1000
learning_rate = 0.01

optim = SGD(model.parameters(), lr=learning_rate)

for epoch in range(N):
    total_loss = 0

    for indx in range(len(inputs)):
        observed = outputs[indx]
        inpt = inputs[indx]
        pred = model(inpt)

        loss = (observed - pred)**2

        loss.backward()
        total_loss += float(loss)

    optim.step()
    optim.zero_grad()


inputs = torch.linspace(start=0., end=1., steps=11)
outputs = model(inputs)

plt.title("Practice Neural Network")
plt.plot(inputs.detach(), outputs.detach(), label="Output")
plt.ylabel("Outputs")
plt.xlabel("Inputs")
plt.legend()
plt.show()
