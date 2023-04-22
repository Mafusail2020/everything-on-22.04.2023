import torch

x = torch.randn(4, requires_grad=True)
print(x)

# x.requires_grad_(False)
# y = x.detach()

y = x+1
print(y)

z = (y * y) / 2
print(z)
i = z * 2
i = i.mean()
print(i)
i.backward()
print(x.grad)
