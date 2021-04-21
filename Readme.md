# Pravega Github helper

[toc]

This set of scripts speeds up the routine work through *initialization*, *pull request* and *clean up*.

It also generate the issue branch and commit message according to the [Pravega Contributing Wiki](https://github.com/pravega/pravega/wiki/Contributing).

```mermaid
graph TD
    id1[Is this issue related to the current repository?]
    id2[Is issue open?]
    id3[Currently on the issue branch?]
    id4[Initialization]
    id5[Pull Request]
    id6[Clean Up]

    id1 -- Yes --> id2
    id2 -- Open --> id3
    id3 -- Yes --> id5
    id3 -- No, on other branch --> id4
    id2 -- Closed --> id6
```

## Initialization

```mermaid
graph TD
    id1[On master branch?]
    id2[Is working directory clean?]
    id3[Stash current files]
    id4[Checkout to master branch]
    id5[Pull upstream master]
    id6[Create a new branch with the issue name]
    id7[Set origin branch to track this new branch]

    id1 -- Yes --> id5
    id1 -- No, on other branch --> id2
    id2 -- Yes --> id4
    id2 -- No, has some files modified --> id3
    id3 --> id4 --> id5
    id5 --> id6 --> id7
```

## Pull Request

```mermaid
graph TD
    id1[Currently on the issue branch?]
    id2[Modified something?]
    id3[Commit with the signature and an appropriate name]
    id4[Push]
    id5[Open Pull Request in the browser]

    id1 -- Yes --> id2
    id2 -- Yes --> id3
    id3 --> id4 --> id5
```

## Clean up

```mermaid
graph TD
    id1[Currently on the issue branch?]
    id2[Checkout to master]
    id3[Delete origin branch]
    id4[Delete local branch]
    id5[Pull upstream master]

    id1 -- Yes --> id3
    id1 -- No --> id2
    id2 --> id3
    id3 --> id4 --> id5
```

# Getting Started

1. Install Python >= 3.7
2. Install third packages via `pip install requests GitPython`
3. Change `ISSUE_URL` and `WORKING_DIR` in `./constants.py`
4. Run `python router.py`
