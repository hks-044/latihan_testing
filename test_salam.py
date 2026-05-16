from salam import halo

def test_halo_berhasil():
    assert halo("Budi") == "Halo Budi"

def test_halo_gagal():
    assert halo("Andi") == "Halo Andi"
