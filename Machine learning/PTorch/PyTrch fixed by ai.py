import torch
import torch.nn as nn
from torch.optim import SGD

import matplotlib.pyplot as plt
import seaborn as sns


# СВЕРХУ ВНИЗ | СПРАВА НАЛЕВО

class BasicNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.w00 = nn.Parameter(torch.tensor(1.7), requires_grad=False)
        self.w01 = nn.Parameter(torch.tensor(-40.8), requires_grad=False)
        self.b00 = nn.Parameter(torch.tensor(-0.85), requires_grad=False)

        self.w10 = nn.Parameter(torch.tensor(12.6), requires_grad=False)
        self.w11 = nn.Parameter(torch.tensor(2.7), requires_grad=False)
        self.b10 = nn.Parameter(torch.tensor(0.0), requires_grad=False)

        self.b01 = nn.Parameter(torch.tensor(-16.0), requires_grad=False)

    def forward(self, inp):
        top_relu_inp = self.w00 * inp + self.b00
        top_relu_out = torch.relu(top_relu_inp)
        scaled_top = top_relu_out * self.w01

        bot_relu_inp = self.w10 * inp + self.b10
        bot_relu_out = torch.relu(bot_relu_inp)
        scaled_bot = bot_relu_out * self.w11

        res = scaled_bot + scaled_top + self.b01
        total = torch.relu(res)

        return total


class BasicNNTrain(nn.Module):
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

        res = scaled_bot + scaled_top + self.b01
        total = torch.relu(res)

        return total


# =====================================================================

inputs = torch.tensor([0., 0.5, 1.])
outputs = torch.tensor([0., 1., 0.])

model = BasicNNTrain()

learning_rate = 0.1
N = 360
b_in_each_epoch = []
w11_in_each_epoch = []
w01_in_each_epoch = []

optimizer = SGD(model.parameters(), lr=learning_rate)

print(f"b01 До обучения = {model.b01.data}\n\n")
epochs = list(range(0, N))

for epoch in range(N):
    total_loss = 0
    for indx in range(len(inputs.detach())):
        observed = outputs[indx]
        # predicted = model.forward(inputs[indx])
        predicted = model(inputs[indx])

        loss = (observed - predicted) ** 2

        loss.backward()

        total_loss += float(loss)

    b_in_each_epoch.append(float(model.b01.data))
    w01_in_each_epoch.append(float(model.w01.data))
    w11_in_each_epoch.append(float(model.w11.data))

    optimizer.step()
    optimizer.zero_grad()

print(len(b_in_each_epoch))
print(f"b01 После обучения = {model.b01.data}.")
print(f"w01 После обучения = {model.w01.data}.")
print(f"w11 После обучения = {model.w11.data}.")

# =====================================================================
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(epochs, b_in_each_epoch, label="b01", color='black')
plt.plot(epochs, w01_in_each_epoch, label="w01", color='blue')
plt.plot(epochs, w11_in_each_epoch, label="w11", color='orange')
plt.ylabel("Arguments")
plt.title("Backpropagation")
plt.xlabel("Epoch")
plt.legend()

# ====================================
plt.subplot(1, 2, 2)
input_set = torch.linspace(start=0, end=1, steps=11)
plt.title("Result")
outs = model(input_set)
sns.lineplot(x=input_set,
             y=outs.detach(),
             color='green',
             linewidth=3)

plt.ylabel("Effictiveness")
plt.xlabel("Dose")

plt.show()
