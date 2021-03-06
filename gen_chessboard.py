import random
from cairosvg import svg2png
import chess.svg
import chess
from PIL import Image, ImageOps


# Ici, i est le numero de l'image. Pour chaque image i un nombre aléatoire j de pièces sont positionnées sur l'échiquier. Pour chaque image i_j, une pièce k est rajoutée
# Ainsi, k etant compris entre 0 et 7; k est le nombre de difference avec l'image img_i_j_0
# Le dossier img_chess regroupe l'ensemble des images différentes concaténées

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


nb_img = 25

for i in range(nb_img):
    board = chess.Board('8/8/8/8/8/8/8/8 w - - 0 1')
    nb_pieces = random.randint(5, 25)
    nb_ajout = 8
    for j in range(nb_pieces):
        piece = random.choice(['Q', 'K', 'N', 'B', 'R', 'P', 'q', 'k', 'n', 'b', 'r', 'p'])
        list_squares = random.sample(range(0, 63), 63)
        square = list_squares.pop(0)  # pourquoi faire du random sur du random ?
        board.set_piece_at(square=square, piece=chess.Piece.from_symbol(piece))
    board_svg = chess.svg.board(board, coordinates=False)
    svg2png(bytestring=board_svg, write_to=f"./board_png/chess_{i}_{0}.png")
    im01 = Image.open(f'./board_png/chess_{i}_{0}.png')
    im1 = ImageOps.expand(im01, border=30)
    get_concat_h(im1, im1).save(f'./img_chess/img_{76 + i}_{0}.png')

    for k in range(1, nb_ajout):
        piece = random.choice(['Q', 'K', 'N', 'B', 'R', 'P', 'q', 'k', 'n', 'b', 'r', 'p'])
        list_squares = random.sample(range(0, 63), 63)
        square = list_squares.pop(0)
        board.set_piece_at(square=square, piece=chess.Piece.from_symbol(piece))
        board_svg = chess.svg.board(board, coordinates=False)
        svg2png(bytestring=board_svg, write_to=f"./board_png/chess_{i}_{k}.png")

        im02 = Image.open(f'./board_png/chess_{i}_{k}.png')
        im2 = ImageOps.expand(im02, border=30)
        get_concat_h(im1, im2).save(f'./img_chess/img_{76 + i}_{k}.png')
    print(f"Image n°{i}")