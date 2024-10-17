class GiangVien :
    def __init__(self , hoTen , namSinh , dsMonHoc):
        self.hoTen = hoTen
        self.namSinh = namSinh
        self.dsMonHoc = dsMonHoc
    def getdsMonHoc (self) :
        return self.dsMonHoc
    def demSoMonHoc (sefl , loai) :
        return len ([mh for mh in sefl.getdsMonHoc() if mh.checkSameType(loai)])
       # return sum (1 for mh in sefl.getdsMonHoc () if mh.checkSameType(loai))
    def tongSoTinChi (self) :
        return sum ([x.getSoTC() for x in self.getdsMonHoc()])
    def __str__(self):
        return self.hoTen +" " + str(self.namSinh)
    def getHoTen (self) :
        return self.hoTen
class MonHoc :
    def __init__(self , maSo , ten , soTinChi , loai):
        self.maSo = maSo
        self.ten = ten
        self.soTinChi = soTinChi
        self.loai = loai
    def checkSameType (self , otherType) :
        return self.loai == otherType
    def getLoai (self ) :
        return self.loai
    def getSoTC (self) :
        return self.soTinChi
    def getTen (self) :
        return self.ten
class Khoa :
    def __init__(self , ten , diaChi , dsgv):
        self.ten = ten
        self.diaChi = diaChi
        self.dsgv = dsgv
    def timGiangVienDayNhieuTinChiNhat (self) :
        return max(self.dsgv , key = lambda gv : gv.tongSoTinChi())
    def thongKeMonHocTheoLoai (self ) :
        # dct  = {}
        # setMonHoc = set()
        # for gv in self.dsgv :
        #     for mh in gv.getdsMonHoc() :
        #         setMonHoc.add(mh)
        # for mh in setMonHoc :
        #     dct[mh.getLoai()] = dct.get(mh.getLoai(), [])
        #     dct[mh.getLoai()].append(mh.getTen())
        # return dct

        listMH = set([mh for gv in self.dsgv for mh in gv.getdsMonHoc()])
        return {k: list(mh.getTen() for mh in listMH if mh.getLoai() == k)
                for k in set(mh.getLoai() for mh in listMH)}
    def timMonHoc(self, tenGiangVien, loai):
            return sorted(set([mh.getTen() for gv in self.dsgv if gv.getHoTen() == tenGiangVien
                               for mh in gv.getdsMonHoc() if mh.getLoai() == loai]), key=lambda tenMH: tenMH)


mon1 = MonHoc (123 , "HCSDL" ,3 , "CNTT")
mon2 = MonHoc (234 , "python" ,4 , "CNTT")
mon3 = MonHoc (452 , "ai" ,4 , "CNTT")
gv1 = GiangVien ("Nguyen Van A" , 1992 , [mon1, mon2])
gv2 = GiangVien ("Nguyen Van B" , 1992 , [mon1, mon2 , mon3])
k = Khoa ("CNTT" , "Thu Duc" , [gv1 , gv2])
print (gv1.demSoMonHoc("CNTT"))
print (k.timGiangVienDayNhieuTinChiNhat())
print (k.thongKeMonHocTheoLoai())
print(k.timMonHoc("Nguyen Van A" , "CNTT"))