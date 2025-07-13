{
 description = "A Nix flake based python development environment";

   inputs = {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    };

    outputs = {self, nixpkgs, ...}:
      let
        system = "x86_64-linux";
      in {
        devShells."${system}".default = 
          let
            pkgs = import nixpkgs {
              inherit system;
            };
          in pkgs.mkShell {
            packages = with pkgs; [
            python313Full
            python313Packages.tkinter
            python313Packages.pandas
            python313Packages.numpy
            jupyter-all
            nodejs_24
            fish 
          ];

          shellHook = ''
            exec fish
          '';
        };
      };
  }
