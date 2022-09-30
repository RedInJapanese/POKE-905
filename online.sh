git clone https://github.com/RedInJapanese/POKE-905.git

cd POKE-905
cd pokemon
chmod +x run.sh
./run.sh

cd ..
rustc test.rs
./test

rm test
cd ..
rm -rf POKE-905