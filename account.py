# INSERT INTO `account` VALUES (1,'pham','abc@gmail.com','$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',3.21,'UET','IT','www.b.a.com','linkedin.com','01235',0,'link.com'),\
#     (2,'tran','tran@gmail.com','$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',2.42,'UED','Giaoduc','www.siu.com','linkedin.com/siu','0294085',0,'siu.com'),\
#     (3,'le','abcd@gmail.com','$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',4,'UEB','Kinthe','www.eco.com',NULL,NULL,0,NULL);
import random

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

ho = ['Tran', 'Ngo', 'Le', 'Ly', 'Phan', 'Vo', 'Dinh', 'Pham', 'Do', 'Nguyen', 'Truong', 'Trinh', 'Hoang', 'Chu', 'Duong', 'Vu', 'Dang']
dem = ['Van', 'Thi', 'Bao', 'Minh', 'Mai', 'Dinh', 'Anh', 'Manh', 'Ma', 'Hoang', 'Le', 'Gia', 'Dang', 'Quoc', 'Binh', 'Nam']
ten = ['Anh', 'An', 'Ba', 'Chau', 'Chi', 'Duc', 'Ha', 'Hanh', 'Khuong', 'Khang', 'Khanh', 'Loc', 'Nam', 'Ngan', 'Ngoc', 'Phuc', 'Phi', 'Quoc', 'Quy', 'Sy', 'Thanh', 'Tam', 'Viet', 'Yen']
school = [['Truong Đai hoc Khoa hoc Tu nhien', 'Toan hoc',
'Toan hoc (CTĐT tai nang)',
'Toan hoc (CTĐT tien tien)',
'Toan co',
'Toan - Tin',
'Khoa hoc May tinh va thong tin (CTĐT thi diem)',
'Khoa hoc du lieu (CTĐT thi diem)',
'Vat ly hoc',
'Vat ly hoc (CTĐT tai nang)',
'Vat ly hoc (CTĐT chuan quoc te)',
'Khoa hoc vat lieu',
'Cong nghe ky thuat hat nhan',
'Ki thuat dien tu va tin hoc (CTĐT thi diem)',
'Hoa hoc',
'Hoa hoc (CTĐT tai nang)',
'Hoa hoc (CTĐT tien tien)',
'Cong nghe ky thuat hoa hoc',
'Cong nghe ky thuat hoa hoc (CTĐT CLC)',
'Hoa duoc (CTĐT CLC)',
'Sinh hoc',
'Sinh hoc (CTĐT chuan quoc te)',
'Sinh hoc (CTĐT tai nang)',
'Cong nghe sinh hoc',
'Cong nghe sinh hoc (CTĐT CLC)',
'Đia ly tu nhien',
'Đia ly tu nhien (CTĐT CLC)',
'Khoa hoc thong tin dia khong gian (CTĐT thi diem)',
'Quan ly dat dai',
'Quan ly phat trien do thi va bat dong san (CTĐT thi diem)',
'Khoa hoc moi truong',
'Khoa hoc moi truong (CTĐT tien tien)',
'Khoa hoc moi truong (CTĐT CLC)',
'Cong nghe ky thuat moi truong',
'Cong nghe ky thuat moi truong (CTĐT CLC)',
'Khoa hoc va cong nghe thuc pham (CTĐT thi diem)',
'Khi tuong va khi hau hoc',
'Hai duong hoc',
'Tai nguyen va moi truong nuoc (CTĐT thi diem)',
'Đia chat hoc',
'Đia chat hoc (CTĐT CLC)',
'Đia chat hoc (CTĐT chuan quoc te)',
'Ky thuat dia chat',
'Quan ly tai nguyen va moi truong',
'Khoa hoc dat',
'Khi tuong hoc (CTĐT CLC)',
'Thuy van',
'Thuy van (CTĐT CLC)',
'Hai duong hoc (CTĐT CLC)',
'Cong nghe quan trac va giam sat tai nguyen moi truong (CTĐT thi diem)'],
          ['Truong Đai hoc Khoa hoc Xa hoi va Nhan van', 'Bao chi',
'Bao chi (CTĐT CLC)',
'Chinh tri hoc',
'Cong tac xa hoi',
'Đong Nam A hoc',
'Đong phuong hoc',
'Han Quoc hoc',
'Han Nom',
'Khoa hoc quan ly',
'Khoa hoc quan ly (CTĐT CLC)',
'Lich su',
'Luu tru hoc',
'Ngon ngu hoc',
'Nhan hoc',
'Nhat Ban hoc',
'Quan he cong chung',
'Quan li thong tin',
'Quan li thong tin (CTĐT CLC)',
'Quan tri dich vu du lich va lu hanh',
'Quan tri khach san',
'Quan tri van phong',
'Quoc te hoc',
'Quoc te hoc (CTĐT CLC)',
'Tam ly hoc',
'Thong tin - thu vien',
'Ton giao hoc',
'Triet hoc',
'Van hoa hoc',
'Van hoc',
'Viet Nam hoc',
'Xa hoi hoc',],
          ['Truong Đai hoc Ngoai ngu', 'Su pham tieng Anh',
'Ngon ngu Anh (CTĐT CLC)',
'Ngon ngu Nga',
'Ngon ngu Phap (CTĐT CLC)',
'Su pham tieng Trung Quoc',
'Ngon ngu Trung Quoc (CTĐT CLC)',
'Su pham Tieng Đuc',
'Ngon ngu Đuc (CTĐT CLC)',
'Su pham tieng Nhat',
'Ngon ngu Nhat (CTĐT CLC)',
'Su pham tieng Han Quoc',
'Ngon ngu Han Quoc (CTĐT CLC)',
'Ngon ngu Arap'],
          ['Truong Đai hoc Cong nghe', 'Cong nghe thong tin',
'Cong nghe thong tin (CTĐT CLC)',
'Cong nghe thong tin dinh huong thi truong Nhat Ban',
'Ky thuat may tinh',
'Ky thuat Robot (CTĐT thi diem)',
'Ky thuat nang luong (CTĐT thi diem)',
'Vat ly ky thuat',
'Co ky thuat',
'Cong nghe ky thuat xay dung',
'Cong nghe Hang khong vu tru (CTĐT thi diem)',
'Ky thuat dieu khien va tu dong hoa',
'Cong nghe nong nghiep (CTĐT thi diem)',
'Cong nghe ky thuat co dien tu (CTĐT CLC)',
'Khoa hoc May tinh (CTĐT CLC)',
'He thong thong tin (CTĐT CLC)',
'Mang may tinh va truyen thong du lieu (CTĐT CLC)',
'Cong nghe ky thuat dien tu - vien thong (CTĐT CLC)',
'Tri tue nhan tao'],
          ['Truong Đai hoc Kinh te', 'Quan tri kinh doanh (CTĐT CLC)',
'Tai chinh - Ngan hang (CTĐT CLC)',
'Ke toan (CTĐT CLC)',
'Kinh te quoc te (CTĐT CLC)',
'Kinh te (CTĐT CLC)',
'Kinh te phat trien (CTĐT CLC)',
'Quan tri kinh doanh (CTĐT danh cho cac tai nang the thao)'],
          ['Truong Đai hoc Giao duc', 'Su pham Toan hoc',
'Su pham Vat ly',
'Su pham Hoa hoc',
'Su pham Sinh hoc',
'Su pham khoa hoc tu nhien',
'Su pham Ngu van',
'Su pham Lich su',
'Su pham lich su va dia li',
'Quan tri truong hoc',
'Quan tri cong nghe giao duc',
'Quan tri chat luong giao duc',
'Tham van hoc duong',
'Khoa hoc giao duc',
'Giao duc tieu hoc',
'Giao duc mam non'],
          ['Truong Đai hoc Viet - Nhat', 'Nhat Ban hoc',
'Khoa hoc va Ky thuat may tinh (CTĐT CLC)',
'Nong nghiep thong minh va ben vung (CTĐT CLC)',
'Ky thuat xay dung (CTĐT CLC)'],
          ['Truong Đai hoc Y Duoc', 'Y khoa',
'Duoc hoc',
'Rang - Ham - Mat (CTĐT CLC)',
'Đieu duong',
'Ki thuat hinh anh y hoc',
'Ki thuat xet nghiem y hoc'],
          ['Truong Đai hoc Luat', 'Luat',
'Luat (CTĐT CLC)',
'Luat kinh doanh',
'Luat thuong mai quoc te'],
          ['Truong Quoc te', 'Kinh doanh quoc te (CTĐT thi diem)',
'Ke toan, phan tich va kiem toan (CTĐT thi diem)',
'He thong thong tin quan li (CTĐT thi diem)',
'Phan tich du lieu kinh doanh (CTĐT thi diem)',
'Marketing (CTĐT cap bang ĐH cua ĐHQGHN va truong ĐH HELP – Malaysia)',
'Quan ly (CTĐT cap bang ĐH cua ĐHQGHN va truong ĐH Keuka – Hoa Ky)',
'Tin hoc va ki thuat may tinh (CTĐT LKQT do ĐHQGHN cap bang)',
'Ngon ngu Anh (chuyen sau Kinh doanh va Cong nghe thong tin)',
'Ky su Tu dong hoa va tin hoc',
'Cong nghe thong tin ung dung',
'Cong nghe tai chinh va kinh doanh so',
'Ky thuat he thong cong nghiep va Logistics'],
          ['Truong Quan tri va Kinh doanh', 'Quan tri doanh nghiep va cong nghe',
'Marketing va Truyen thong',
'Quan tri Nhan luc va Nhan tai',
'Quan tri va An ninh',],
          ['Khoa Cac khoa hoc lien nganh', 'Quan tri thuong hieu (CTĐT thi diem)',
'Quan tri tai nguyen va di san (CTĐT thi diem)',
'Quan ly giai tri va su kien',
'Quan tri do thi thong minh va ben vung']]

f = open("account.txt", "a", encoding="utf-8")
# f.write("Now the file has more content!")
# f.close()

f.write("INSERT INTO `account` VALUES ")
for x in range(4, 1638): #1638
    truong = random.choice(school)
    nganh = truong[random.randint(1, len(truong)-1)]
    ten_truong = truong[0]
    # print('(' + str(x) + ','
    #     + "'" + random.choice(ho) + ' ' + random.choice(dem) + ' ' + random.choice(ten) + "',"
    #     + "'19020" + f"{x:03}" + "@vnu.edu.vn'," + "'$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',"
    #     + str(round(random.uniform(2.00, 3.99), 2)) + ','
    #     + "'" + ten_truong + "',"
    #     + "'" + nganh + "',"
    #     + 'NULL,'
    #     + random.choice([("'" + 'www.linkedin.com/' + "19020" + f"{x:03}" + "',"), ('NULL,')])
    #     + "'0" + str(random.randint(100000000, 999999999)) + "',"
    #     + '0,'
    #     + 'NULL),' + '\n'
    #      )

    f.write('(' + str(x) + ','
          + "'" + random.choice(ho) + ' ' + random.choice(dem) + ' ' + random.choice(ten) + "',"
          + "'19020" + f"{x:03}" + "@vnu.edu.vn'," + "'$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',"
          + str(round(random.uniform(2.00, 3.99), 2)) + ','
          + "'" + ten_truong + "',"
          + "'" + nganh + "',"
          + 'NULL,'
          + random.choice([("'" + 'www.linkedin.com/' + "19020" + f"{x:03}" + "',"), ('NULL,')])
          + "'0" + str(random.randint(100000000, 999999999)) + "',"
          + '0,'
          + 'NULL),' + '\n'
          )

# f.close()
# INSERT INTO `account` VALUES (1,'pham','abc@gmail.com','$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',3.21,'UET','IT','www.b.a.com','linkedin.com','01235',0,'link.com'),\
#     (2,'tran','tran@gmail.com','$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',2.42,'UED','Giaoduc','www.siu.com','linkedin.com/siu','0294085',0,'siu.com'),\
#     (3,'le','abcd@gmail.com','$2b$10$qH0hVjno/.SRCWBArUgfD.xkolTN9g0gPEGqSqJd0DrDLOxxqwn9W',4,'UEB','Kinthe','www.eco.com',NULL,NULL,0,NULL);