from textnode import *



def main():
    node = TextNode('THIS IS SOME TEXT', TextType.LINK, 'https://boot.dev')
    print(node.__repr__)

main()