# df

Code/docs repository for the DF lab.

---

## Installation Instructions

## Step 1 — Install Git

Git is a version control system. This is how we will save and share code for the project. 

1. Go to https://git-scm.com/download
2. Follow the instructions for your operating system (OS)



---

## Step 2 — Download this code to your computer

To copy the code to your computer so you can run it, you need to "clone" it.

1. Open your terminal
- On Windows, open the taskbar search and type "Terminal"
- On Mac, open the Spotlight search (command + space bar) and type "Terminal"
- On Linux, press `CTL + ALT + T`
2. In the terminal, type the following command and press `Enter`:
   ```
   git clone https://github.com/freemocap/df.git
   ```
- This will create a `df` folder in your computers "home" path. If you want it installed somewhere else, you need to navigate to the desired folder first. You can learn to do that with [these instructions]](https://terminalcheatsheet.com/guides/navigate-terminal)
3. You'll see some text scroll by. When it finishes, a new folder called `df` has been created on your computer.
4. Now move into that folder by typing this command and pressing `Enter`:
   ```
   cd df
   ```
   (`cd` stands for "change directory" — it moves you into a folder.)

---

## Step 3 — Install uv

`uv` is a tool that manages Python and the code's dependencies. It has some overlap with other tools like `conda` which you may have heard of, but is newer.

You can download `uv` following the instructions on their [getting started page](https://docs.astral.sh/uv/getting-started/installation/)


---

## Step 4 — Run the code

To run any Python file, use `uv run` followed by the path to the file.

1. Make sure you're inside the `df` folder in your terminal. (If you just followed Step 2, you already are. If you opened a new terminal, type `cd df` and press `Enter` first.)
2. Type the following command and press `Enter`:
   ```
   uv run df/main.py
   ```
   (`df/main.py` is the path to the file — `df` is the folder it lives in, and `main.py` is the file name.)
3. You should see:
   ```
   Hello from df!
   ```

To run a different file, just replace `df/main.py` with the path to that file. For example, if there was a file called `df/analysis.py`, you would run `uv run df/analysis.py`.

