{
 description = "My second flake!";

   inputs = {
      nixpkgs.url = "github.nixos/nixpkgs/nixos-unstable";
    };

    outputs = {self, nixpkgs, ...}: 
    
    let

      pkgs = nixpkgs.legacyPackages."x86_64-linux";
    
      # if a python package is not packaged in nix use pip2nix
      # $ nix run github:nix-community/pip2nix -- generate packagename_in_pip_format
      # this generates python-packages.nix and use with this flake by uncommenting lines below
      # packageOverrides = pkgs.callPackages. ./python-packages.nix {};
      # python = pkgs.python3.override { inherit packageOverrides; };

    in {
      devShells.x86_64-linux.default = pkgs.mkShell {

        packages = [
          (pkgs.python313.withPackages(p: with p; [
            tkinter
            numpy
          ]))
        ];

      };
    };
  }
