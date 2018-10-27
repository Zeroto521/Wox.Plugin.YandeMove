# Wox.Plugin.YandeMove

Auto collect yande.re's pictures to one folder where you like.

![screenshots](/Images/zero_20181027_115544.png)

## Example

### before

It looks like **mess**.

> ![screenshots](/Images/zero_20181027_115705.png)

### after

**Clear**, now.

> ![screenshots](/Images/zero_20181027_115859.png)

## Setting

1. Install `Wox`.
2. Install `Wox.Plugin.YandeMove`.
3. Open the **Plugin** folder.
4. Open the **yandeMove.py** file.
5. Find the `RAW_PATH_LIST` and add path which you want to move.

## Attention

Once there are the **same** picture(by **name**) between **AIM_PATH** and **RAW_PATH**, this program will send the picture in RAW_PATH to **win system recycle** not **delete**.

## Requirements

1. `Python3.x`
2. `shutil`
3. `send2trash`
