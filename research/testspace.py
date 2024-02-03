from music_generator.utilities import save_weights
model = "dsfs"
epochs = 100
save_freq = 10
for epoch in range(epochs):
    print('\nEpoch {}/{}'.format(epoch + 1, epochs))
    losses, accs = [], []
    
    if (epoch + 1) % save_freq == 0:
        save_weights(epoch + 1, model)
        print('Saved checkpoint to', 'weights.{}.h5'.format(epoch + 1))