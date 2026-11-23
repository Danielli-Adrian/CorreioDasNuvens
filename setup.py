import cx_Freeze

executaveis = [
    cx_Freeze.Executable(
        script="main.py",
        icon="bases/icone.ico",
        target_name="CorreioDasNuvens.exe",
    )
]

cx_Freeze.setup(
    name="Correio das Nuvens",
    options={
        "build_exe": {
            "packages": ["pygame", "pyttsx3"],
            "include_files": ["bases", "recursos"],
        }
    },
    executables=executaveis,
)