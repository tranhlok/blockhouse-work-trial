import torch.nn as nn

# Model
class TransformerModel(nn.Module):
    def __init__(self, input_dim, num_classes, d_model=32, nhead=4, num_layers=4, dim_feedforward=256):
        super(TransformerModel, self).__init__()
        self.transformer = nn.Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_layers,
                                          dim_feedforward=dim_feedforward, batch_first=True)
        self.fc = nn.Linear(d_model, num_classes)
        self.embedding = nn.Linear(input_dim, d_model)

    def forward(self, x):
        x = self.embedding(x).unsqueeze(1)  # Add sequence dimension
        x = self.transformer(x, x)
        x = self.fc(x[:, -1])
        return x