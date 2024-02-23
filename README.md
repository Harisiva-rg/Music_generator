# Music Generation with CharRNN and MLOps Pipeline

This project presents a music generation pipeline powered by a Char-RNN model. The Char-RNN model, trained on a comprehensive  dataset of ABC notation, predicts the next musical symbol given a preceding sequence.

## Key Technologies:

- **Char-RNN:** Processes ABC music as a sequence of characters.
- **MLOps Pipeline:** Modular structure with automated stages for data pre-processing, model building, model training, and music generation.
- **Music21 Integration:** Seamless conversion of generated ABC notation to MIDI files for audio playback.

## Project Highlights:

- **Modular and Maintainable:** Code organized into distinct modules for clarity and extensibility.
- **Automated Workflow:** MLOps pipeline practice is followed to streamline the process from development to deployment.
- **Comprehensive Logging:** Every stage and its outcome is  performance analysis and debugging.
- **Data Management:** Organized data structure ensures reproducibility and integrity.
- **Package Distribution:** setup.py allows easy installation as a Python package. 

**Note:** The above template was created using my PyPI package [dsforge](https://pypi.org/project/dsforge/).


## Usage:

- Clone the repository: `git clone https://github.com/Harisiva-rg/Music_generator`
- Install dependencies: `pip install -r requirements.txt`
- Run the pipeline: `python main.py`
- Model generates a midi file that can be found inside **Exports** directory 
- To generate a new melody using the existing model, modify the **SEED** and **NUM_CHARS** values in the **Constants** module and run `stage_04_generatenotes.py`.


Here is one of the sample tunes generated by the model.

<audio controls>
  <source src="exports/Composed_music.mid" type="audio/midi">
  Your browser does not support the audio element [Try here!](exports/Composed_music.mid).
</audio>

## License:

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Contribution:
Feel free to contribute to this project or use it for your learning and experimentation!


