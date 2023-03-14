# CALCULATOR

Simple calculator made by a teenager addicted to shitpost.

## How to use

Press buttons to do operations and other stuff, or use keys instead (key_binds.txt).

## Important information

I'm not smart enough to make this work like a normal calculator, so if you want to use any of the following operations, you'll have to have a number (and not an
operation) on the input box, and THEN click the operation button:

- Factorial (!)
- Sine (sin)
- Cosine (cos)
- Tangent (tan)
- Square root (√)
- Cube root (∛)
- Logarithm (log)

## How to convert to an executable

- Download the code as a zip file and unzip it to a folder

- Open that folder with the terminal

- Run this command:
` pip install pyinstaller `

- And lastly, run this one:
` pyinstaller --onedir --noconsole --noconfirm --name "Calculator" --icon "icon.ico" --add-data "icon.ico;." --add-data "key_binds.txt;." --add-data "log.txt;." --add-data "README.md;." main.py `

- Open the dist folder and run the app.
