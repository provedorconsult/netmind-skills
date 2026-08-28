# G03 Rotation policy

Parameters `max-size`, `max-file`, retention and safety margin are derived from
capacity, growth, traffic, diagnostic retention and recovery objectives.
Expected maximum: `eligible log containers × max-size × max-file`, adjusted for
exceptions. Values remain parameters until approved by the environment owner.
