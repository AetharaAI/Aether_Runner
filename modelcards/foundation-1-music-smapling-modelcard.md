
Foundation-1
Structured text-to-sample generation for modern music production
Overview

Foundation-1 is a next-generation text-to-sample model designed around musical structure. It was trained to understand instrumentation, timbre, FX, and notation as separate composable controls. This gives musicians and producers direct control over not just instrument identity, but also sonic character, phrase behavior, musical feel, and loop structure.

The result is a model built for actual production workflows: tempo-synced, key-aware, bar-aware sample generation with strong musicality, strong prompt adherence, and unusually high timbral flexibility.

Foundation-1 is designed for pure sample generation. It excels at generating coherent musical loops that stay locked to tempo and phrase length while allowing layered prompting across instrument families, timbre descriptors, FX, and notation-driven musical behavior.
What Foundation-1 Does

    Generates musically coherent loops for production workflows
    Understands BPM and bar count for structured loop generation
    Locks to major and minor keys across western music theory
    Supports enharmonic equivalents when prompting scales and keys
    Separates instrument identity from timbral character
    Supports timbral mixing by combining instrument and sonic descriptors
    Responds to FX tags such as reverb, delay, distortion, and modulation
    Uses notation-style prompt structure to encourage coherent phrasing, melodic shape, rhythmic behavior, and harmonic motion
    Produces perfect loops within supported BPM / bar denominations
    Understands Wet vs Dry production context — adding terms like Dry encourages minimal FX processing, while Wet or FX tags produce more processed, spatial, or effected sounds.

Why It Feels Different

Most audio models can react to broad prompt terms like “warm pad” or “bright synth.” with inconsistent results. Foundation-1 was designed to go further by treating the sound as a layered system:

    Instrument Family – what broad source category the sound belongs to
    Sub-Family – the more specific instrument role or identity
    Timbre Tags – the tonal, spectral, or textural character
    FX Tags – the processing layer applied to the sound
    Notation / Structure Tags – the musical behavior of the generated phrase

This layered conditioning approach is a major reason Foundation-1 is able to deliver both high musicality and high prompt control at the same time.
Audio Showcase
Prompt 	Audio
Bass, FM Bass, Medium Delay, Medium Reverb, Low Distortion, Phaser, Sub Bass, Bass, Upper Mids, Acid, Gritty, Wide, Dubstep, Thick, Silky, Warm, Rich, Overdriven, Crisp, Deep, Clean, Pitch Bend, 303, 8 Bars, 140 BPM, E minor 	
Sub Bass, Bass, Gritty, Small, Square, Bass, Dark, Digital, Thick, Clean, Simple, Bassline, Epic, Choppy, Melody, 4 Bars, 150 BPM, G# minor 	
Flute, Pizzicato, Punchy, Present, Ambient, Nasal, Melody, Epic, Airy, Slow Speed, 8 Bars, 150 BPM, E minor 	
High Saw, Spacey, Lead, Warm, Silky, Smooth, 303, Synth Lead, Medium Reverb, Low Distortion, Upper Mids, Mids, Pitch Bend, Arp, 8 Bars, 140 BPM, F minor 	
Trumpet, Warm, Complex Arp Melody, High Reverb, Low Distortion, Smooth, Silky, Texture, 8 Bars, 130 BPM, C minor 	
Synth, Pad, Chord Progression, Rising, Digital, Bass, Fat, Near, Wide, Silky, Warm, Focused, 8 Bars, 110 BPM, D major 	
Piccolo, Flute, Airy, Music Box, plucked, complex melody, 8 Bars, 140 BPM, C# minor 	
Synth Lead, Wavetable Bass, Low Distortion, High Reverb, Sub Bass, Upper Mids, Acid, Gritty, Wide, Thick, Silky, Warm, Rich, Overdriven, Crisp, Clean, 303, Complex, 8 Bars, 140 BPM, F minor 	
Fiddle, Bowed Strings, Full, Clean, Spacey, Rich, Intimate, Thick, Rolling, Arp, Fast Speed, Complex, 8 Bars, 128 BPM, B minor 	
Chiptune, Chord Progression, Pulse Wave, Medium Reverb, 8 Bars, 128 BPM, D minor 	
Kalimba, Mallet, Medium Reverb, Overdriven, Wide, Metallic, Thick, Sparkly, Upper Mids, Bright, Airy, Alternating, Chord Progression, Atmosphere, Spacey, Fast Speed, 8 Bars, 120 BPM, B minor 	
Core Capabilities
1. Musical Structure

Foundation-1 was trained to produce structured musical material rather than full music or generic textures. Musical Notation terms can encourage notation, chord progressions, melodies, arps, phrase direction, rhythmic density, and other musically relevant behaviors.
2. Instrument Identity

The model supports a broad instrument hierarchy spanning synths, keys, basses, bowed strings, mallets, winds, guitars, brass, vocals, and plucked strings.
3. Timbral Control

Foundation-1 is not limited to broad instrument naming. It also responds to timbral descriptors such as spectral shape, tone, width, density, texture, brightness, warmth, grit, space, and other sonic traits.
4. Timbral Mixing

Because instrument identity and timbral character were not collapsed into a single flat label, the model is especially strong at timbral hybridization and layered sonic prompting.
5. FX Prompting

The model supports a dedicated FX layer covering multiple forms of reverb, delay, distortion, phaser, and bitcrushing.
6. Loop Fidelity

Foundation-1 is built for production-ready loop generation, including BPM-aware and bar-aware structure within supported denominations.
Conditioning Architecture

Foundation-1 was trained with a layered tagging hierarchy designed to improve control, composability, and prompt clarity.
Hierarchy Overview

    Major Family → broad instrument class
    Sub-Family → more specific instrument role
    Timbre Tags → tonal / spectral / textural descriptors
    FX Tags → processing layer
    Notation Tags → musical behavior and phrasing

This makes it possible to prompt at different levels of abstraction. A user can stay broad with a family-level prompt like Synth or Keys, or get more specific with terms like Synth Lead, Wavetable Bass, Grand Piano, Violin, or Trumpet, then further shape the output using timbral and FX descriptors.
Instrument Coverage
Major Families

Foundation-1 was trained across the following major instrument families:

    Synth
    Keys
    Bass
    Bowed Strings
    Mallet
    Wind
    Guitar
    Brass
    Vocal
    Plucked Strings

Sub-Family Coverage

Foundation-1 includes a wide sub-family layer covering a broad range of production-relevant instrument roles, including but not limited to:

    Synth Lead
    Synth Bass
    Digital Piano
    Pluck
    Grand Piano
    Bell
    Pad
    Atmosphere
    Digital Strings
    FM Synth
    Violin
    Digital Organ
    Supersaw
    Wavetable Bass
    Rhodes Piano
    Cello
    Texture
    Flute
    Reese Bass
    Wavetable Synth
    Electric Bass
    Marimba
    Trumpet
    Pan Flute
    Choir
    Harp
    Church Organ
    Acoustic Guitar
    Hammond Organ
    Celesta
    Vibraphone
    Glockenspiel
    Ocarina
    Clarinet
    French Horn
    Tuba
    Oboe

Sub-Family Chart
Timbre System

One of Foundation-1’s main strengths is that it was not trained to treat timbre as an afterthought. Timbral character is directly represented in the prompt system, giving users control over not only what is being generated, but also how it sounds.

Representative timbre descriptors include:

    Warm
    Bright
    Wide
    Airy
    Thick
    Rich
    Tight
    Full
    Gritty
    Clean
    Retro
    Saw
    Crisp
    Focused
    Metallic
    Chiptune
    Dark
    303
    Shiny
    Analog
    Present
    Sparkly
    Ambient
    Soft
    Smooth
    Cold
    Buzzy
    Deep
    Formant Vocal
    Round
    Punchy
    Nasal
    Vintage
    Growl
    Breathy
    Glassy
    Noisy
    Synthetic Vox
    Supersaw
    Bitcrushed
    Dreamy

Timbre Chart
Why This Matters

This tagging design makes prompts much more flexible. Instead of only asking for an instrument, users can shape:

    tonal balance
    brightness / darkness
    width / intimacy
    clean vs driven character
    synthetic vs organic feel
    transient sharpness
    texture and density
    spatial character

This is especially useful for producers who want to guide the output toward a specific role in a mix rather than just a generic instrument label.

For a list of used tags please see the Tag Reference Sheet.
FX Layer

Foundation-1 includes a dedicated FX descriptor layer spanning multiple common production effects.

Representative FX tags include:

    Low Reverb
    Medium Reverb
    High Reverb
    Plate Reverb
    Low Delay
    Medium Delay
    High Delay
    Ping Pong Delay
    Stereo Delay
    Cross Delay
    Mono Delay
    Low Distortion
    Medium Distortion
    High Distortion
    Phaser
    Low Phaser
    Medium Phaser
    High Phaser
    Bitcrush
    High Bitcrush

FX Chart
Musical Notation and Structure

Foundation-1 was trained with structured musical descriptors designed to improve phrase coherence, rhythmic intent, melodic motion, and prompt control.

These notation-style prompt terms help steer:

    chord progressions
    melodies
    top-line layers
    arpeggios
    phrase direction
    rhythmic density
    harmonic feel
    subdivision style
    simple vs complex motion
    sustained vs plucked behavior
    melodic contour and pacing

Examples of supported structural ideas may include terms such as:

    chord progression
    melody
    top melody
    arp
    triplets
    simple
    complex
    rising
    falling
    strummed
    sustained
    catchy
    epic
    slow
    fast

This notation layer is one of the main reasons Foundation-1 produces unusually coherent musical material instead of static or loosely related phrases. These can be mixed and matched as desired.
Tonal and Timing Support

Foundation-1 is designed for structured music production workflows and supports:
Keys and Modes

    Major keys
    Minor keys
    Enharmonic equivalents
    Western 12-tone chromatic prompting

Loop Structure

    Supported bar lengths: 4 Bars, 8 Bars
    Supported BPM denominations: 100 BPM, 110 BPM, 120 BPM, 128 BPM, 130 BPM, 140 BPM, 150 BPM

Prompt Structure

For best results, use rich prompts built around the model’s tags. These tags can be mixed and matched as needed. The model was trained on a structured hierarchy designed to encourage musically coherent sample generation.
Layered Prompt Structure

[Instrument Family / Sub-Family], [Timbre], [Musical Behavior / Notation], [FX], [Key], [Bars], [BPM]
Prompting Notes

    Start with a clear instrument identity
    Add 1–3 timbre descriptors for stronger steering
    Include a notation or musical structure term for better phrase coherence
    Always include Bars and BPM, which define the musical loop length
    Ensure the generation duration matches the requested musical structure
    The RC Stable Audio Fork automatically handles this timing alignment

Use FX and timbre tags sparingly at first, then layer more once you understand the model’s behavior.
One Prompt → Multiple Outputs

Each row below uses the exact same prompt, but a different random seed.
The timbre tags remain unchanged, so the overall sound character stays consistent while the melodic and musical content varies between generations.
Prompt 	Output A 	Output B 	Output C
Bass, FM Bass, Medium Delay, Medium Reverb, Low Distortion, Phaser, Acid, Gritty, Wide, Dubstep, Thick, Silky, Warm, Rich, Overdriven, Crisp, Deep, Clean, Triplets, 8 Bars, 150 BPM, A minor 	
	
	
Gritty, Acid, Bassline, 303, Synth Lead, FM, Sub, Upper Mids, High Phaser, High Reverb, Pitch Bend, 8 Bars, 140 BPM, E minor 	
	
	
Kalimba, Mallet, Medium Reverb, Overdriven, Wide, Metallic, Thick, Sparkly, Upper Mids, Bright, Airy, Small, Alternating Chord Progression, Atmosphere, Spacey, Fast, 4 Bars, 120 BPM, B minor 	
	
	
Recommended Workflow

Foundation-1 is best used with the RC Stable Audio Fork, which is tuned around this model’s metadata and prompting structure.

It provides:

    random prompt generation aligned with the training tags
    automatic MIDI extraction from generated audio
    automatic BPM / bar timing alignment for loop generation

Recommended Interfaces

RC Stable Audio Tools (Enhanced Fork)

Stable Audio Tools (Original Repository)
Model Files

In the folder you will find two files: the model itself and its associated config.json.

Unlike prior releases where both 32-bit and 16-bit models were provided, this release includes only the 16-bit version.

There is no quality loss, while reducing the model footprint.

    Foundation_1.safetensors
    model_config.json

Basic Setup for usage in the RC Enhanced Fork

    Create a subfolder inside your models directory
    Place the model checkpoint and config file inside that folder
    Launch the interface
    Select the model from the UI
    Prompt with layered musical descriptors for best results

Hardware Requirements

Foundation-1 is designed to run locally on modern GPUs.

Typical VRAM usage during generation is approximately ~7 GB.
For reliable operation, a GPU with at least 8 GB of VRAM is recommended.
Generation Performance

Generation speed will vary depending on GPU model and system configuration.

On an RTX 3090, generation time is approximately ~7–8 seconds per sample.
Dataset and Training Philosophy

Foundation-1 was built around a structured sample-generation philosophy, rather than generic or genre-based audio captioning. The dataset consists entirely of hand-crafted and labeled audio, produced through a controlled augmentation pipeline.

At a high level, the training design emphasizes:

    structured musical loops
    instrument hierarchy
    explicit timbre representation
    dedicated FX descriptors
    notation-aware prompt terms
    strong production relevance
    broad reuse for compositional workflows

This design is central to the model’s musical coherence and high degree of sonic control.

For more details on the dataset and training methodology, see the Training & Dataset Notes.
Limitations

Foundation-1 is a specialized model for music sample generation, not a general-purpose music generator.

Important notes:

    It performs best when prompted using vocabulary aligned with the training design
    It is optimized for sample-generation workflows, not open-ended genre captioning
    Only two genre tags were included (Dubstep Growls and Chiptune waveforms), primarily to reinforce waveform behaviors
    Prompt quality matters — structured layered prompts outperform vague natural language
    Some timbre tags exert stronger influence than others
    Certain tag combinations may require iteration to achieve the exact musical role or timbral blend desired
    Percussion and drum sounds are outside the scope of this release

The model is also optimized around specific timing relationships between Bars, BPM, and generation duration.

For example:

    an 8-bar loop at 100 BPM ≈ 19 seconds

If the generation duration is shorter than the musical structure implied by the prompt (for example requesting an 8-bar loop but generating only 5 seconds), the model may produce less coherent musical phrases.

The RC Stable Audio Fork automatically handles this timing alignment, making this workflow much easier.
License

This model is licensed under the Stability AI Community License. It is available for non-commercial use or limited commercial use by entities with annual revenues below USD $1M. For revenues exceeding USD $1M, please refer to the repository license file for full terms.
Companion Video

Further information on the model and design philosophy can be found in the companion video:

🎥 Watch the Foundation-1 overview and design philosophy video
Final Notes

Foundation-1 is intended as a producer-facing foundation model for structured sample generation, designed to augment music production rather than replace it.

Its goal is to let users explore sound in new ways while retaining precise control over:

    what the sound is
    how it behaves musically
    how it sits tonally
    how it feels sonically
    how it fits into a production workflow

That combination of musical structure, instrument identity, timbral control, and loop fidelity is what defines the model.
