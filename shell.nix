{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python313.withPackages(p: with p; [
      tkinter
    ]))
   ];

}
