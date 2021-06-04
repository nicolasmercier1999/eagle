from RV1.models import Document_Type, Permission_Type, User, Classroom, Module, Chapter, Course, Group

# Document_Type

doc_type = ["PDF", "Word", "Excel", "PowerPoint", "Source C / C++", "Header C / C++", "Fichier Java", "Fichier Python", "Fichier CSV", "Fichier C#", "Fichier texte", "Autre"]

for typedc in doc_type:
	doc = Document_Type(dct_type=typedc)
	doc.save()

# Permission_Type

per_type = ["Télécharger", "Lire", "Modifier"]

for typepr in per_type:
	per = Document_Type(prt_name=typepr)
	per.save()

# User

genre = [False, True, True, True, True, False, True, False, False, False, True, False, False, True, True, True, True, False, False, False, True, True, False, True]
prenom = ["Jean", "Amanda", "Marie", "Sarah", "Diane", "Laurent", "Aurore", "Etienne", "David", "Pascal", "Myriam", "Rémi", "Bruno", "Anne", "Cécile", "Mathilde", "Ludivine", "Antoine", "Pierre", "Damien", "Annie", "Carole", "Harold", "Janet"]
nom = ["DUPOND", "HOLZ", "DELANOE", "SWIFT", "MARCHAL", "DUMAIS", "GAMBOIS", "BELLANGER", "MARCHAND", "DUBOIS", "LAMBERT", "GALLOIS", "MAZZERI", "VANDERMOORE", "PASQUIER", "QUARRIER", "BOLET", "DUCHEMIN", "KELLERMANN", "WIENE", "WINTER", "BARRIER", "DUBREUIL", "JOLIVET"]
mail = ["jean.dupond@edu.esiee.fr", "amada.holz@edu.esiee.fr", "marie.delanoe@edu.esiee.fr", "sarah.swift@edu.esiee.fr", "diane.marchal@edu.esiee.fr", "laurent.dumais@edu.esiee.fr", "aurore.gambois@edu.esiee.fr", "etienne.bellanger@edu.esiee.fr", "david.marchand@edu.esiee.fr", "pascal.dubois@edu.esiee.fr", "myriam.lambert@edu.esiee.fr", "remi.gallois@edu.esiee.fr", "bruno.mazzeri@edu.esiee.fr", "anne.vandernoore@edu.esiee.fr", "cecile.pasquier@edu.esiee.fr", "mathilde.quarrier@edu.esiee.fr", "ludivine.bolet@edu.esiee.fr", "antoine.duchemin@edu.esiee.fr", "pierre.kellermann@esiee.fr", "damien.wiene@esiee.fr", "annie.winter@esiee.fr", "carole.barrier@esiee.fr", "harold.dubreuil@esiee.fr", "janet.jolivet@esiee.fr"]
active = [True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, False, False, True, True, True, True, True, False]
root = ["drive.google.com/drive/u/1/my-drive/dupondj", "drive.google.com/drive/u/1/my-drive/holza", "drive.google.com/drive/u/1/my-drive/delanoem", "drive.google.com/drive/u/1/my-drive/swifts", "drive.google.com/drive/u/1/my-drive/marchald", "drive.google.com/drive/u/1/my-drive/dumaisl", "drive.google.com/drive/u/1/my-drive/gamboisa", "drive.google.com/drive/u/1/my-drive/bellangere", "drive.google.com/drive/u/1/my-drive/marchandd", "drive.google.com/drive/u/1/my-drive/duboisp", "drive.google.com/drive/u/1/my-drive/lambertm", "drive.google.com/drive/u/1/my-drive/galloisr", "drive.google.com/drive/u/1/my-drive/mazzerib", "drive.google.com/drive/u/1/my-drive/vandermoorea", "drive.google.com/drive/u/1/my-drive/pasquierc", "drive.google.com/drive/u/1/my-drive/quarrierm", "drive.google.com/drive/u/1/my-drive/quarrierm", "drive.google.com/drive/u/1/my-drive/duchemina", "drive.google.com/drive/u/1/my-drive/kellermannp", "drive.google.com/drive/u/1/my-drive/wiened", "drive.google.com/drive/u/1/my-drive/wintera", "drive.google.com/drive/u/1/my-drive/barrierc", "drive.google.com/drive/u/1/my-drive/dubreuilh", "drive.google.com/drive/u/1/my-drive/jolivetj"]
dates = ["2000-01-01", "2000-05-13", "1999-11-07", "2000-01-11", "1999-04-30", "1999-01-18", "1999-03-22", "1998-10-10", "2000-02-06", "2000-06-28", "1999-12-27", "1998-09-06", "2001-01-15", "2001-03-19", "2000-09-24", "1998-11-20", "1997-08-14", "1997-02-06", "1977-07-03", "1989-08-14", "1980-02-24", "1988-11-09", "1981-07-03", "1977-09-28"]

for i in range(len(genre)):
	usr = User(
		usr_gender = genre[i],
		usr_firstname = prenom[i],
		usr_lastname = nom[i],
		usr_email = mail[i],
		usr_active = active[i],
		usr_root_dir = root[i],
		usr_birth_date = dates[i]
		)
	usr.save()

# Classroom

class_nom = ["4309", "4301+", "5401", "5403", "2305", "2306"]
class_capacite = ["28", "60", "30", "28", "20", "10"]

for i in range(len(class_nom)):
	cls = Classroom(
		cls_name = class_nom[i],
		cls_capacity = class_capacite[i]
		)
	cls.save()

# Module

mod_nom = ["Programmation Orientée Objet", "Deep Learning", "Programmation Réseaux", "Systèmes d’exploitation", "Technical Writing", "Infographie 3D", "C++", "Skills Consolidation", "Business English", "Python", "Java"]
mod_start = ["2020-09-03", "2020-09-03", "2020-09-03", "2020-09-03", "2020-09-03", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01"]
mod_end = ["2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-07-02", "2021-07-02", "2021-07-02", "2021-07-02", "2021-07-02", "2021-07-02"]

for i in range(len(mod_nom)):
	mod = Module(
		mdl_name = mod_nom[i],
		mdl_start_date = mod_start[i],
		mdl_end_date = mod_end[i]
		)
	mod.save()

# Chapter

modul_id = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11]
chap_id = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 1, 2]
chap_titre = ["Introduction", "Concepts de la POO", "Projet", "Introduction", "Les réseaux de neurones", "Optimisation des réseaux", "Introduction", "Couches réseau", "Les communications inter-applications", "Introduction", "Lecture / écriture dans les fichiers", "Les threads", "Les lettres", "Les rapports", "Les gizmos", "Mesh, collider et rigidbody", "Classes", "Surcharge d’opérateurs", "STL", "Tenses", "Temporal benchmarks", "Reports", "Mailing", "Présentation", "Les fonctions système", "Projet : jeu du morpion", "Les fonctions système", "Projet : jeu Tron"]

for i in range(len(modul_id)):
	mod_instance = Module.objects.get(id = modul_id[i])
	chp = Chapter(
		mdl = mod_instance,
		chp_id = chap_id[i],
		chp_title = chap_titre[i]
		)
	chp.save()

# Course

module_id = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 11]
chapter_id = [1, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 2, 3, 1, 2, 2, 3, 3, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 3, 3, 1, 2, 1, 2, 3, 3, 1, 2, 2, 1, 2, 2]
course_id = [1, 1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2]
course_nom = ["Histoire de la POO", "Classes", "Interactions entre classes", "Jeu d’échecs séance 1", "Jeu d’échecs séance 2", "Jeu d’échecs séance 3", "Introduction", "Les réseaux de neurones", "Optimisation des réseaux", "Histoire des réseaux", "Les couches 1 à 3", "Les couches 4 à 7", "TD 1", "Introduction", "fread", "fwrite", "Threads (1)", "Threads (2)", "Écriture de lettres", "Rédaction de rapports", "Utilisation des gizmos", "Mesh", "Collider", "Rigidbody", "Méthodes et attributs", "Opérateurs", "Opérateurs arithmétiques", "Opérateurs de flux", "Opérateurs d’accès", "Maps, listes et vectors", "Iterator", "Preterit & Past participle", "Future", "Writing a report", "Formatting a professional email", "Preparing a slideshow", "Presenting a slideshow", "Fonctions système de Python", "Jeu du morpion – TP", "Jeu du morpion – Soutenance", "Fonctions système de Java", "Jeu Tron – TP", "Jeu Tron – Soutenance"]
course_start = ["2020-09-10 10:00:00", "2020-09-17 10:00:00", "2020-09-24 10:00:00", "2020-10-01 09:00:00", "2020-10-08 09:00:00", "2020-10-15 09:00:00", "2020-09-08 13:00:00", "2020-09-15 14:00:00", "2020-09-22 13:00:00", "2020-09-09 08:00:00", "2020-10-22 15:00:00", "2020-10-29 15:00:00", "2020-11-05 09:00:00", "2020-09-17 15:00:00", "2020-09-24 15:00:00", "2020-10-01 15:00:00", "2020-10-08 15:00:00", "2020-10-15 15:00:00", "2020-12-01 13:00:00", "2020-12-08 13:00:00", "2020-12-02 08:00:00", "2020-12-09 08:00:00", "2020-12-16 08:00:00", "2020-12-23 08:00:00", "2020-12-03 10:00:00", "2020-12-10 10:00:00", "2020-12-15 10:00:00", "2020-12-16 10:00:00", "2020-12-17 10:00:00", "2020-12-18 10:00:00", "2020-12-18 14:00:00", "2021-02-04 14:00:00", "2021-02-11 14:00:00", "2021-02-04 14:00:00", "2021-02-11 14:00:00", "2021-02-18 14:00:00", "2021-02-25 14:00:00", "2021-06-01 10:00:00", "2021-06-08 10:00:00", "2021-06-15 10:00:00", "2021-06-01 14:00:00", "2021-06-08 14:00:00", "2021-06-15 14:00:00"]
course_end = ["2020-09-10 12:00:00", "2020-09-17 12:00:00", "2020-09-24 12:00:00", "2020-10-01 12:00:00", "2020-10-08 12:00:00", "2020-10-15 12:00:00", "2020-09-08 15:00:00", "2020-09-15 18:00:00", "2020-09-22 16:00:00", "2020-09-09 11:00:00", "2020-10-22 18:00:00", "2020-10-29 18:00:00", "2020-11-05 13:00:00", "2020-09-17 17:00:00", "2020-09-24 17:00:00", "2020-10-01 17:00:00", "2020-10-08 17:00:00", "2020-10-15 17:00:00", "2020-12-01 15:00:00", "2020-12-08 15:00:00", "2020-12-02 12:00:00", "2020-12-09 12:00:00", "2020-12-16 12:00:00", "2020-12-23 12:00:00", "2020-12-03 12:00:00", "2020-12-10 12:00:00", "2020-12-15 12:00:00", "2020-12-16 12:00:00", "2020-12-17 12:00:00", "2020-12-18 12:00:00", "2020-12-18 18:00:00", "2021-02-04 16:00:00", "2021-02-11 16:00:00", "2021-02-04 16:00:00", "2021-02-11 16:00:00", "2021-02-18 16:00:00", "2021-02-25 16:00:00", "2021-06-01 12:00:00", "2021-06-08 12:00:00", "2021-06-15 12:00:00", "2021-06-01 18:00:00", "2021-06-08 18:00:00", "2021-06-15 18:00:00"]
course_content = ["Donec tristique magna vitae libero rutrum aliquet. Praesent molestie fringilla nisi, at pretium leo interdum et. Sed nec commodo nisl. Donec diam dui, egestas eu mauris sed, tempor gravida arcu. Cras varius pretium pellentesque. Aenean metus nisl, egestas id enim vel, venenatis varius justo. Ut at justo elit. Curabitur eu maximus arcu. Mauris eu est ac quam volutpat efficitur sed aliquam sapien.", "Nunc in fermentum est, a pretium purus. Nam rutrum vehicula massa, et ullamcorper justo vehicula sit amet. Vestibulum sit amet lacinia nulla. Aliquam sit amet mattis turpis. Vivamus pellentesque sit amet libero id venenatis. Aenean scelerisque leo sit amet nibh malesuada, sed venenatis quam convallis. Integer in fermentum lectus. Cras mollis sapien libero, non sollicitudin sapien egestas in. Duis commodo enim lacus, vitae pulvinar lorem facilisis quis. Nullam sed elit metus. Nam euismod nisi id massa porttitor, nec semper libero pharetra. Sed eu tincidunt erat.", "Phasellus efficitur purus sit amet nulla vehicula pellentesque. Donec nulla nisl, suscipit et luctus nec, malesuada sit amet ante. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean viverra est sed ex tincidunt aliquet. Nunc vitae nunc id risus posuere eleifend a quis tellus. Aliquam leo ante, accumsan sit amet facilisis sed, aliquet in enim. Duis ut accumsan justo. Vivamus viverra velit at tristique scelerisque. Maecenas neque lectus, iaculis vitae iaculis ut, maximus eu nisl. Aenean varius ac lacus eu volutpat.", "Cras dignissim convallis maximus. Nullam sit amet sodales velit. Fusce nec metus non massa semper fringilla. Morbi pharetra molestie sapien eget aliquam. Morbi commodo mattis diam, sed varius nisi pellentesque id. Vivamus ante tortor, dapibus ac hendrerit et, lobortis et lacus. Integer tortor sem, aliquet in arcu at, venenatis ornare leo. Duis at ex rhoncus, scelerisque tellus eu, volutpat dolor. Duis sollicitudin est ut quam vehicula varius. Suspendisse at metus vel mi tempus tristique. Cras blandit, mauris nec consectetur convallis, magna lacus aliquet nisl, a pellentesque magna risus at lorem. Pellentesque enim turpis, rutrum nec libero faucibus, aliquam consequat erat. Suspendisse a ante in velit luctus congue eget ut sem. Nunc tempus porta tellus. Nulla facilisi.", "Integer dictum est vel placerat viverra. Fusce non ultrices dui. Mauris in tellus neque. Ut luctus in nulla sit amet rutrum. Donec eu leo mi. Proin ac maximus sem. Pellentesque vitae tempor felis, eu placerat dui. In eget est tincidunt dolor efficitur rutrum. Donec id aliquam quam, sed rutrum nibh.", "Etiam venenatis elit luctus diam convallis, quis vestibulum sem rhoncus. Curabitur ut tellus a mauris ultrices sodales. Integer pellentesque gravida turpis id accumsan. Praesent iaculis dictum lorem vitae venenatis. Duis iaculis condimentum nulla sed gravida. Proin purus ipsum, maximus eu consectetur sit amet, sodales sed dolor. Nunc sapien eros, ullamcorper sed rutrum at, gravida at sapien. Vestibulum et feugiat mi. In nec tincidunt quam, rutrum dapibus enim. Integer in rhoncus mi. Proin vestibulum egestas pulvinar. Aliquam sit amet ligula varius, sollicitudin leo ac, ultricies tortor. Duis at magna nec ipsum cursus mollis.", "Sed aliquam ante at magna viverra, sit amet tristique odio congue. Pellentesque vitae rutrum tellus, sit amet blandit leo. Aliquam eget lectus non ante malesuada posuere sed ac urna. Donec feugiat imperdiet mi, eget viverra dui varius vitae. Pellentesque tincidunt sapien diam, a fermentum quam pellentesque ut. Nam a risus orci. Ut lacinia nisl eu hendrerit finibus. Aenean vehicula molestie magna, a ullamcorper metus rutrum quis. Fusce tristique mollis tortor, sed congue eros accumsan id. Nulla vel risus in nulla lacinia tincidunt. Aliquam ac ornare tortor. Vestibulum a est laoreet, tincidunt elit et, maximus quam.", "Donec interdum egestas facilisis. Pellentesque eu ultrices sem. Sed sed felis tristique, sagittis purus vel, volutpat dui. Mauris felis massa, bibendum sit amet accumsan at, sollicitudin vitae metus. Sed augue magna, hendrerit quis lacus in, cursus ultrices nisl. Quisque luctus dolor ac purus finibus, ac mollis tellus venenatis. In tincidunt molestie tellus, sit amet dictum dolor viverra quis. Curabitur mollis nulla non lectus vehicula scelerisque. Phasellus vel gravida ex. Nam ac vestibulum quam. Vestibulum varius, arcu vel efficitur consectetur, nisi diam sodales elit, ac ornare tellus nisi ac velit. Etiam faucibus leo sed lacus maximus, ut tincidunt ligula consequat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum viverra enim a ipsum dictum, quis malesuada nisl consectetur. Praesent laoreet massa eros, at sollicitudin magna elementum volutpat.", "Cras quis sem eget erat molestie posuere eget et arcu. Morbi at ullamcorper orci. Phasellus facilisis nisl molestie urna suscipit, sed ultrices diam rutrum. Vestibulum eleifend gravida libero et aliquet. In viverra, ante at scelerisque viverra, risus arcu imperdiet elit, vitae viverra metus libero id ante. Nullam et justo vitae nunc iaculis tristique. Quisque in quam at est pretium ullamcorper. Nam ut pellentesque quam, eget efficitur ligula. Mauris placerat eros a justo mattis, nec hendrerit purus elementum. Aenean suscipit scelerisque condimentum. Maecenas malesuada arcu dolor, vel consequat diam ornare in. Vestibulum mattis ac arcu vel faucibus. Quisque porta risus vel justo volutpat, a elementum erat sagittis. Nulla vel tellus sagittis, ultricies justo vel, ultrices massa.", "Nam eget ultrices sapien, ut ultrices sapien. Etiam sit amet leo dapibus, malesuada quam eget, placerat neque. Integer eget dignissim odio. Duis molestie quam sapien, a pharetra quam dignissim in. Donec id placerat orci, id tincidunt magna. In aliquam, leo sit amet suscipit tempor, mauris neque porttitor velit, nec viverra libero neque quis mi. Nullam volutpat leo id lectus dignissim, eget facilisis felis sodales. Mauris ut venenatis sem.", "Quisque viverra eros ac ante eleifend, eu placerat neque tincidunt. Quisque viverra elit a accumsan maximus. Aenean feugiat id nulla in cursus. Morbi metus odio, elementum id enim sed, euismod eleifend ligula. Proin id lacus tempor, laoreet neque eu, scelerisque eros. In lacus odio, hendrerit eget sapien in, eleifend lacinia neque. Proin congue ullamcorper lorem eu vestibulum. Fusce luctus ante eu tempor convallis. In non dapibus sem, vel rhoncus libero. Donec sed nunc maximus, maximus tortor at, ornare purus.", "Mauris sollicitudin dolor at augue finibus, at vehicula ante consectetur. Morbi facilisis metus lectus, vel efficitur sem tincidunt ut. Donec commodo mattis lorem ut gravida. Donec metus dolor, rutrum eu congue in, dictum at enim. Aenean a efficitur sapien. Suspendisse at ex viverra, efficitur massa quis, dictum ipsum. Praesent eleifend tortor eu elementum ultricies. In hac habitasse platea dictumst. Aenean finibus pulvinar nulla quis scelerisque. Nunc auctor non dolor nec bibendum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.", "Aenean blandit luctus urna a facilisis. Duis quis ultrices ipsum. Quisque sodales aliquet odio, non luctus eros auctor sit amet. Duis elementum lacus eu viverra auctor. Nulla interdum dictum erat, sed convallis dui auctor eget. Ut lectus felis, vulputate eget nisl ac, volutpat blandit lorem. Suspendisse sit amet augue cursus, blandit nulla ac, vulputate orci. Praesent nibh ante, facilisis ac scelerisque luctus, dictum eget turpis. Etiam turpis felis, viverra nec ligula ac, iaculis venenatis nulla. Integer vitae blandit magna. In hac habitasse platea dictumst. Praesent mollis ornare lacus varius efficitur. Etiam eu lectus ac dolor imperdiet facilisis. Fusce sit amet malesuada massa. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id purus in sapien posuere mollis.", "Aliquam sed convallis orci, ac porta ligula. Integer non orci eget sem suscipit porta. Nullam enim lacus, suscipit a fermentum eu, interdum id tellus. Vestibulum auctor diam a vehicula imperdiet. Proin dictum sit amet enim sed tristique. Proin tempus sit amet massa vitae finibus. Nam quis dictum massa. Nullam quis est enim. Mauris elementum ornare eros ut egestas. Quisque sit amet imperdiet erat. Donec urna nisi, vehicula eget arcu ac, maximus varius metus. In tempus dapibus massa, at aliquet lectus consectetur vel.", "Sed posuere dui in magna tempus, eu elementum sapien feugiat. Proin scelerisque fermentum quam non pulvinar. Sed non turpis tincidunt, cursus neque non, ullamcorper ligula. Suspendisse placerat tempus orci, sed varius purus mollis ac. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris vehicula diam nec arcu vulputate, non tristique arcu tempus. In vel convallis enim, sit amet iaculis nisl. Phasellus posuere magna risus, non viverra libero aliquet at. Vestibulum consectetur dolor urna, sed pretium ligula cursus vel. Duis placerat finibus lorem ut vestibulum.", "Suspendisse vitae elit porta, tempor arcu et, interdum ante. Cras et arcu erat. Nunc at aliquet tellus. Sed auctor sodales leo, eget suscipit lectus molestie sit amet. Donec elementum leo elit, quis posuere mi iaculis vel. Pellentesque ac elit dolor. Donec ut lacus eu mauris luctus rutrum sit amet ac diam. Sed faucibus lorem non ipsum tempor, non volutpat augue gravida. Quisque pellentesque dui a arcu cursus vestibulum. Suspendisse vulputate eros at diam auctor, ut hendrerit risus gravida. Aenean scelerisque odio eu justo hendrerit, ac elementum mauris auctor.", "Cras dui sem, ultrices at nisi id, sodales fermentum arcu. Nullam ut lorem diam. Sed ut quam at urna tristique mattis. Nullam ullamcorper lorem ut nibh euismod, ut gravida dolor tempor. Praesent consequat diam vitae molestie convallis. Ut at porta neque, nec dictum ipsum. Quisque vel pulvinar lectus, eget commodo erat. Aenean non odio eget tellus tincidunt venenatis. Praesent euismod hendrerit consequat. Sed ac consectetur risus.", "Proin ut dignissim odio. Cras id vulputate tellus. Curabitur porttitor sem vel elit pellentesque, quis aliquam mauris cursus. Cras diam velit, hendrerit a purus vitae, viverra varius justo. Quisque varius fermentum neque, at aliquam arcu suscipit at. Curabitur augue metus, eleifend molestie eleifend vel, posuere tempor ante. Mauris pharetra massa sit amet molestie blandit. Aliquam egestas, nisl ac convallis sagittis, neque erat efficitur purus, a ullamcorper justo nisl vel nisi.", "Morbi vulputate finibus justo eget auctor. Fusce blandit sed lectus sit amet maximus. Fusce tortor erat, consectetur ac ullamcorper vel, venenatis eget dui. Duis euismod quam sed dolor dapibus, nec tempor urna malesuada. Aenean suscipit accumsan ante a varius. Sed consequat pretium nulla, a iaculis enim tincidunt sed. Pellentesque sollicitudin, urna eu facilisis bibendum, dolor justo dapibus enim, id convallis nunc urna in dolor. Suspendisse dictum, purus vel egestas varius, tellus metus venenatis enim, eget congue elit tortor sit amet orci. Phasellus et ipsum id ex eleifend tincidunt ut nec nunc. Donec vulputate lorem id ligula suscipit varius. Aenean non mi vulputate, euismod erat quis, pretium ex. Nunc rutrum leo lacus, commodo pretium tortor viverra nec. Aenean in faucibus ex, vel porta mauris.", "Nam viverra odio ac dui vestibulum mattis. Praesent volutpat molestie faucibus. Curabitur dignissim volutpat ex quis fermentum. Aliquam mollis fermentum velit, ac tincidunt nisi rutrum vitae. Ut nec augue nibh. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris dignissim feugiat bibendum. Morbi pretium egestas nulla ut semper.", "Maecenas porta risus quis mattis mattis. Nunc feugiat mauris et gravida pulvinar. Donec sit amet ante cursus, lacinia magna sed, porta sem. Duis a ipsum orci. Maecenas ac nulla non lorem tristique blandit. Aliquam et tempor neque, eu convallis justo. Fusce fermentum leo ut libero bibendum, at cursus erat vulputate. Aliquam erat volutpat. Nam efficitur tincidunt fermentum. Mauris dui metus, iaculis sed ultricies eu, auctor in nibh. Donec volutpat elementum augue eu efficitur. Maecenas vel laoreet lectus, ac ultrices dui. Praesent vel suscipit ante. In sem mauris, dictum quis est eu, lacinia iaculis sapien. Nullam vehicula dui sed enim suscipit mattis vitae eget mauris.", "Nulla at justo risus. Cras commodo accumsan tincidunt. Suspendisse potenti. Ut vel lorem in eros interdum varius at id quam. Integer quis molestie velit. Suspendisse lacinia, lacus eget iaculis dictum, mauris ligula gravida odio, vitae tincidunt ligula elit at ligula. Mauris lacus lorem, sollicitudin sit amet felis et, suscipit tempor tortor. Maecenas massa sem, vulputate quis nisi id, hendrerit ultrices elit. Curabitur sit amet metus sed nisi sodales faucibus. Cras vitae porta turpis. Etiam sed convallis nibh. Proin sodales lacus vel urna accumsan, et venenatis neque mollis.", "Donec blandit sollicitudin ipsum, pulvinar efficitur velit sagittis at. Nullam et elit orci. Sed faucibus, enim et lobortis efficitur, dui erat imperdiet lacus, suscipit luctus risus leo sed massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer euismod odio ac euismod dictum. Suspendisse maximus quam lacus, vel euismod quam rutrum a. Pellentesque sed tellus sed odio aliquet semper nec ac dui. Curabitur sollicitudin rhoncus dolor vel lobortis. Vestibulum fermentum sollicitudin tellus, vitae auctor ipsum condimentum sed. Phasellus sem nibh, varius sit amet velit eget, bibendum rhoncus magna. Ut sed tincidunt risus. Donec ac ligula ante. Fusce lacinia leo vel mauris tristique maximus. Suspendisse facilisis dolor sit amet libero scelerisque tincidunt. Fusce vestibulum viverra imperdiet.", "Curabitur vel consequat urna. Aliquam erat volutpat. Sed condimentum, enim at eleifend dignissim, tortor justo laoreet orci, ac vestibulum massa justo id erat. Nunc et ornare est. Vivamus nisi urna, consectetur eget ipsum vel, tempor condimentum libero. Quisque in pretium dolor. Sed quis lectus pharetra elit molestie bibendum. Nulla vestibulum in mi at condimentum. Quisque vel neque lectus. Praesent mollis felis ut orci lobortis euismod. Suspendisse volutpat cursus ex, non euismod nulla volutpat eu.", "Nam et felis pretium, ultricies orci a, mollis ex. Nunc felis risus, vulputate eget sapien vitae, sodales mattis ex. Aenean at magna elementum, egestas nisl non, venenatis lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; In lectus dui, vestibulum vel tempus ut, lobortis dignissim augue. Suspendisse dui ante, accumsan a suscipit non, commodo vel orci. Etiam ut orci cursus, sollicitudin lorem a, rhoncus eros. Aenean non pellentesque ipsum. Nulla eu sem sodales, ultricies enim vel, suscipit odio. Cras a mauris vel metus lacinia ullamcorper eu eu urna. Nullam auctor massa sed turpis consectetur feugiat. Morbi vitae sagittis lorem. Praesent accumsan neque et nisl gravida ultrices.", "Nullam luctus rhoncus nibh nec vehicula. Etiam nec velit maximus, maximus neque id, condimentum est. Integer nec suscipit diam. Nulla ornare orci in neque mollis, et auctor orci pretium. Etiam nec mauris et est egestas ornare nec at quam. Donec luctus turpis vitae nibh dictum, quis pellentesque mauris eleifend. Duis auctor tortor efficitur felis auctor, vitae euismod quam dignissim. Sed fringilla in elit a volutpat. Pellentesque facilisis mi quis quam tristique sagittis. Phasellus vulputate tortor nunc, sit amet maximus risus congue in. Duis vitae commodo mauris, eu accumsan ligula. Nullam dignissim lacus a dignissim dictum. Suspendisse non ex pretium, dictum nulla id, commodo quam. Nunc vulputate nunc sed libero condimentum auctor. Nunc justo mi, aliquam in hendrerit ut, tincidunt nec mi.", "Quisque scelerisque ex eros, sit amet faucibus augue porttitor sed. Duis vitae aliquam nunc. Phasellus facilisis congue orci vitae auctor. Vestibulum nibh nibh, semper quis magna fermentum, blandit sodales purus. Praesent vitae erat pellentesque lorem malesuada sodales. Suspendisse potenti. Donec euismod mauris mi, non tempus nunc eleifend et. Fusce vel mi finibus, sodales mi quis, mattis ante. Vivamus nec pharetra nibh. Aliquam ac magna mollis, pulvinar nibh eu, porttitor nibh. Aenean quis dignissim massa. Duis non ligula blandit, ullamcorper arcu ut, varius sem. Nulla at tellus leo. Nulla laoreet mi quis massa venenatis, vitae semper nulla sodales.", "Praesent gravida sollicitudin felis eu imperdiet. Fusce ac dignissim ex, ac malesuada urna. Quisque efficitur blandit augue nec pulvinar. Aliquam molestie velit nunc, vel congue enim finibus eu. Nulla sit amet scelerisque metus. Donec facilisis maximus ligula tincidunt cursus. Mauris scelerisque velit vitae felis viverra finibus. Sed lorem nisi, pretium vitae nunc eget, cursus consequat diam. Suspendisse sed interdum tellus. Nam bibendum lorem nec leo luctus, et tincidunt risus fermentum. Donec commodo velit eget euismod vehicula. Nunc finibus turpis risus, non vulputate lacus convallis et. Mauris pellentesque gravida metus, eu elementum lorem. Donec sit amet enim orci. Pellentesque sed massa tempus, elementum sapien at, tempus nibh. Cras laoreet nibh in leo dignissim euismod.", "Aliquam sit amet viverra magna. Ut mattis rhoncus risus non porta. Pellentesque aliquam est a elit bibendum ullamcorper. Ut mollis dui vulputate arcu fermentum luctus. Nullam fermentum diam massa, eget sagittis ex luctus at. Nunc in massa et tellus finibus placerat. Etiam non sapien at mi gravida molestie. Aliquam nisi enim, ullamcorper faucibus lorem vitae, cursus suscipit augue. Suspendisse porttitor purus in quam vestibulum blandit. Donec sed turpis non tellus venenatis ultricies. Nulla posuere, velit in ultrices ultrices, arcu tellus mollis eros, quis molestie nibh metus in ipsum.", "Nulla rhoncus ac elit sit amet convallis. Proin pharetra a est tempus luctus. Cras vitae risus at sem iaculis euismod. Praesent fringilla leo quis diam vulputate ornare. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi sit amet laoreet tortor, aliquet varius diam. Pellentesque faucibus in dui id maximus. Morbi ornare laoreet venenatis. Nulla facilisi. Nulla facilisi. Aliquam erat volutpat. Praesent ornare dui id fringilla rutrum. Donec facilisis augue nisi, vitae lobortis nisl dignissim eget. Ut diam urna, iaculis id finibus vitae, varius ac mi. Phasellus dapibus nisl orci, ac tristique tellus laoreet in.", "Praesent nunc augue, porta vitae porta nec, tempus at ipsum. Aenean tristique suscipit vulputate. Quisque tincidunt, mauris ut convallis eleifend, dolor leo porttitor purus, at interdum ante lorem eget enim. Integer sed nunc dolor. Quisque dapibus venenatis nulla a feugiat. In lobortis egestas odio at lacinia. Nam gravida sem libero, vel blandit dui cursus a. Curabitur sed condimentum massa. Praesent in nisl bibendum, interdum velit quis, porttitor neque.", "Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce vel dolor a lorem condimentum ornare. Sed quam nibh, euismod non justo vitae, molestie consectetur dolor. Nunc condimentum fringilla tincidunt. Nulla viverra convallis eros in efficitur. Quisque lobortis lacus quis velit sollicitudin pulvinar. Integer nibh diam, cursus sed lacinia ac, varius vitae diam. Fusce dui quam, ultrices id auctor ac, egestas at urna. Nam justo dui, mollis at eleifend quis, pretium eu nunc. Proin lobortis dictum dignissim.", "Proin pellentesque eget augue posuere facilisis. Mauris sit amet diam vel mi porta volutpat. Cras imperdiet aliquam justo quis elementum. Nunc eu augue et dui pellentesque facilisis et vehicula magna. Cras ultrices volutpat erat eget tempus. Vestibulum ac elit nec odio semper mollis ut a mi. Vivamus ac felis a augue sollicitudin volutpat. Fusce dignissim interdum nulla. Sed mattis eget risus in ornare. Pellentesque pulvinar semper sagittis. Integer imperdiet auctor nibh, at auctor erat tempor at. Maecenas nisi justo, pellentesque in nisi non, accumsan molestie nisi.", "Aliquam ullamcorper aliquam tempor. Sed sollicitudin, ipsum et ornare scelerisque, justo mi pellentesque ante, et congue felis ex eu diam. Morbi mollis eros id ex luctus pretium. Etiam lorem velit, maximus sit amet fringilla id, pulvinar id sem. Vivamus magna lectus, egestas at tempus in, bibendum et ipsum. Integer nec tempus odio. Sed placerat ante condimentum tortor ullamcorper blandit. Proin efficitur scelerisque elit, nec elementum nisi molestie non. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus in efficitur metus. Praesent non scelerisque elit. Duis quis est ultrices, volutpat mi eget, interdum urna. Nullam viverra leo id risus sagittis, sed mattis leo porttitor.", "Vivamus faucibus aliquet est, eu blandit tortor egestas at. Donec tristique eleifend pulvinar. Proin a finibus libero. Curabitur a nulla elementum, pharetra arcu a, tristique augue. Cras eu pharetra orci. Integer quis lectus a leo mollis consequat id non sapien. Nulla facilisi. Vestibulum suscipit turpis at lectus tempus maximus. Nunc ornare arcu in lectus rutrum posuere. Cras non bibendum justo. Mauris ipsum lectus, placerat eu quam vel, efficitur accumsan ex. Donec eros ligula, molestie in purus eu, ultrices fermentum justo. Sed dapibus eros vitae augue fermentum varius.", "Nullam tempor nibh dui, eu elementum metus elementum ac. Pellentesque a risus nec nibh luctus ultrices id sed neque. Nullam suscipit gravida ex, rhoncus pulvinar odio varius et. Fusce vitae metus aliquet eros luctus interdum. Etiam consectetur leo libero, sit amet interdum risus eleifend vel. Fusce id mattis massa, et bibendum nibh. Nullam non porta lorem. Phasellus eleifend, tellus id pulvinar cursus, elit nulla sagittis neque, id pulvinar leo arcu eu mauris. Integer porta laoreet vehicula. Nunc suscipit commodo urna, luctus feugiat turpis sodales quis. Proin ultricies mauris tellus, vitae pretium nulla consectetur non. Duis et malesuada nulla. Vivamus rutrum volutpat nibh, a posuere leo faucibus quis.", "In mattis quam sed erat commodo consequat. Nunc et orci sem. Cras lacinia ex eget magna tristique, eget vestibulum eros ullamcorper. Cras suscipit posuere ipsum, eu vestibulum nisi consequat eget. Nulla felis nulla, pellentesque lacinia tellus in, egestas tempus purus. Curabitur posuere, erat sed iaculis rhoncus, nibh metus placerat metus, vitae eleifend mauris elit sed nisl. Phasellus eleifend ultricies arcu a vehicula. Suspendisse venenatis vehicula ligula. In bibendum varius sapien, at luctus ipsum imperdiet sit amet. Donec ac tellus vel velit iaculis pulvinar.", "Integer vulputate sollicitudin enim eu tincidunt. Nunc sagittis commodo libero, sed bibendum dolor cursus et. Nunc sed condimentum turpis, in malesuada diam. Pellentesque tristique ut enim in dapibus. Vestibulum vitae purus nisi. Aliquam quis eros facilisis risus porttitor rhoncus ac ac neque. Vivamus sed nisi eu erat mollis rhoncus. Aliquam ultricies et leo nec auctor. Nulla arcu elit, molestie non feugiat ut, hendrerit at erat. Donec eu blandit lacus. Nullam maximus mi est, eget ullamcorper nibh tincidunt sit amet. Nulla sed enim risus. Nullam sed libero neque.", "Nunc sed suscipit purus, id lobortis tortor. Proin vitae augue efficitur, feugiat massa quis, dictum mauris. Mauris vulputate scelerisque arcu ac accumsan. Vivamus convallis erat sapien, a iaculis mauris fermentum accumsan. Quisque ut libero dolor. Aliquam cursus auctor lectus efficitur efficitur. Integer suscipit diam nulla, eu vestibulum enim feugiat vitae. Pellentesque turpis justo, finibus in placerat vitae, aliquet et tellus. Duis blandit venenatis lectus efficitur blandit. Pellentesque mauris nulla, scelerisque sed sapien id, gravida accumsan quam. Sed massa lacus, maximus a odio id, tempor rutrum est. Sed vitae accumsan urna, a viverra erat. Quisque gravida neque a magna hendrerit, nec finibus ligula fermentum.", "Donec eget pulvinar lacus. Fusce leo lectus, sodales at posuere id, auctor at nulla. Suspendisse aliquam odio non magna volutpat fringilla. Pellentesque sed cursus lectus. Vestibulum tincidunt at orci id accumsan. Maecenas id ante in nisi viverra ullamcorper. Cras commodo tincidunt enim, sed posuere augue hendrerit in. Aenean tincidunt libero ut hendrerit elementum. Nunc eu enim luctus, imperdiet ligula eget, porta dolor. Donec convallis elit velit, quis suscipit nibh eleifend sit amet. Duis efficitur enim non dolor dignissim, sagittis mattis odio condimentum. Duis vel libero ligula. Sed sed odio at ante congue finibus. Nam efficitur nulla diam, nec pulvinar lectus fringilla nec. Praesent viverra urna sit amet nibh sagittis, a feugiat metus laoreet. Praesent vitae odio nec urna pulvinar faucibus.", "Mauris id blandit ipsum. In hac habitasse platea dictumst. Quisque eget pulvinar justo, eget faucibus purus. Sed ut tortor id metus posuere auctor. Nulla semper non diam id placerat. Morbi quis faucibus metus, quis fringilla ligula. Quisque elementum rutrum mauris, aliquet blandit nunc molestie eu.", "Vestibulum eu orci ut massa molestie porta a quis sapien. Etiam at elementum turpis. Pellentesque vitae tellus eu purus elementum dictum ut eget sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer bibendum turpis sit amet sem pharetra ullamcorper non in diam. Vivamus pharetra quam sapien, imperdiet fringilla tellus ullamcorper luctus. Donec sit amet dolor eget turpis efficitur viverra. Vivamus varius ex sed commodo elementum. Etiam hendrerit turpis quis lectus tempor, maximus dictum neque ultrices. Proin feugiat aliquet tortor, elementum suscipit enim elementum sed. Suspendisse nec egestas lacus. Nam scelerisque vel turpis id tincidunt. Fusce posuere elit elit, vel sodales tellus ultricies nec.", "In lacinia, lorem quis faucibus hendrerit, neque leo mollis nisl, in ornare felis ante eu urna. Donec volutpat felis et ipsum volutpat dictum at non dolor. Praesent feugiat velit lorem. Phasellus ultricies eget justo nec venenatis. Phasellus quis ligula a urna lacinia ornare in vehicula metus. Nullam convallis ante at mi dapibus, non tristique odio vestibulum. Sed justo augue, varius non augue cursus, porta consectetur est. Maecenas lobortis justo at lorem consequat pulvinar. Proin nec leo sit amet sem ultrices auctor quis sed eros. Morbi accumsan blandit ex a egestas. Aliquam id purus risus. Integer commodo magna quis justo facilisis, vel facilisis mi vestibulum. Fusce tincidunt diam nec tempor elementum. Integer blandit mollis aliquet."]
course_classe = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1]
course_prof = [19, 19, 19, 19, 19, 19, 20, 20, 20, 19, 19, 19, 19, 21, 21, 21, 21, 21, 22, 22, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 23, 23, 23, 23, 20, 20, 20, 21, 21, 21]

for i in range(len(module_id)):
	m_id = Module.objects.get(id = module_id[i])
	c_id = Chapter.objects.get(id = chapter_id[i])
	prof = User.objects.get(id = course_prof[i])
	classe = Classroom.objects.get(id = course_classe[i])
	crs = Course(
		mdl = m_id,
		chp = c_id,
		crs_id = course_id[i],
		crs_name = course_nom[i],
		crs_start_datetime = course_start[i],
		crs_end_datetime = course_end[i],
		crs_content = course_content[i]
		)
	crs.save()
	crs.crs_classroom.add(classe)
	crs.crs_teacher.add(prof)

# Group

ggroup_code = ["GENERAL", "2021S1E", "2021S1P", "2021S1E3", "2021S1E3FI", "2021S1E3FI-GRP1", "2021S1E3FI-GRP2", "2021S1E3FE", "2021S1E3FE-GRP1", "2021S1E3FE-GRP2", "2021S1E4", "2021S1E4FI", "2021S1E4FI-GRP1", "2021S1E4FI-GRP2", "2021S1E4FE", "2021S1E4FE-GRP1", "2021S1E4FE-GRP2", "2021S1FI", "2021S1FE", "2021S1E3ANG", "2021S1E3ANGA", "2021S1E3ANGB", "2021S1E4ANG", "2021S1E4ANGA", "2021S1E4ANGB", "2021S2E", "2021S2P", "2021S2E3", "2021S2E3FI", "2021S2E3FI-GRP1", "2021S2E3FI-GRP2", "2021S2E3FE", "2021S2E3FE-GRP1", "2021S2E3FE-GRP2", "2021S2E4", "2021S2E4FI", "2021S2E4FI-GRP1", "2021S2E4FI-GRP2", "2021S2E4FE", "2021S2E4FE-GRP1", "2021S2E4FE-GRP2", "2021S2FI", "2021S2FE", "2021S1E4ANG", "2021S1E4ANGA", "2021S1E4ANGB", "2021S2E4ANG", "2021S2E4ANGA", "2021S2E4ANGB"]
group_name = ["Général", "2020-2021 S1 Etudiants", "2020-2021 S1 Professeurs", "2021-2021 S1 E3", "2021-2021 S1 E3FI", "2020-2021 S1 E3FI Groupe 1", "2020-2021 S1 E3FI Groupe 2", "2021-2021 S1 E3FE", "2020-2021 S1 E3FE Groupe 1", "2020-2021 S1 E3FE Groupe 2", "2021-2021 S1 E4", "2021-2021 S1 E4FI", "2020-2021 S1 E4FI Groupe 1", "2020-2021 S1 E4FI Groupe 2", "2021-2021 S1 E4FE", "2020-2021 S1 E4FE Groupe 1", "2020-2021 S1 E4FE Groupe 2", "2020-2021 S1 FI", "2020-2021 S1 FE", "2020-2021 S1 E3 Anglais", "2020-2021 S1 E3 Anglais Groupe A", "2020-2021 S1 E3 Anglais Groupe B", "2020-2021 S1 E4 Anglais", "2020-2021 S1 E4 Anglais Groupe A", "2020-2021 S1 E4 Anglais Groupe B", "2020-2021 S2 Etudiants", "2020-2021 S2 Professeurs", "2021-2021 S2 E3", "2021-2021 S2 E3FI", "2020-2021 S2 E3FI Groupe 1", "2020-2021 S2 E3FI Groupe 2", "2021-2021 S2 E3FE", "2020-2021 S2 E3FE Groupe 1", "2020-2021 S2 E3FE Groupe 2", "2021-2021 S2 E4", "2021-2021 S2 E4FI", "2020-2021 S2 E4FI Groupe 1", "2020-2021 S2 E4FI Groupe 2", "2021-2021 S2 E4FE", "2020-2021 S2 E4FE Groupe 1", "2020-2021 S2 E4FE Groupe 2", "2020-2021 S2 FI", "2020-2021 S2 FE", "2020-2021 S2 E3 Anglais", "2020-2021 S2 E3 Anglais Groupe A", "2020-2021 S2 E3 Anglais Groupe B", "2020-2021 S2 E4 Anglais", "2020-2021 S2 E4 Anglais Groupe A", "2020-2021 S2 E4 Anglais Groupe B"]
group_start = ["0001-01-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2020-08-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01", "2021-02-01"]
group_end = ["9999-12-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-01-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31", "2021-07-31"]
group_usr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 17, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 9, 10, 11, 12, 1, 2, 3, 4, 1, 2, 3, 4, 9, 10, 11, 12, 9, 10, 11, 12, 5, 6, 7, 8, 13, 14, 15, 16, 5, 6, 7, 8, 5, 6, 7, 8, 13, 14, 15, 16, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 9, 10, 11, 12, 1, 3, 9, 11, 2, 4, 10, 12, 5, 6, 7, 8, 13, 14, 15, 16, 5, 7, 13, 15, 6, 8, 14, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 9, 10, 11, 12, 1, 2, 3, 4, 1, 2, 3, 4, 9, 10, 11, 12, 9, 10, 11, 12, 5, 6, 7, 8, 13, 14, 15, 16, 5, 6, 7, 8, 5, 6, 7, 8, 13, 14, 15, 16, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 9, 10, 11, 12, 1, 3, 9, 11, 2, 4, 10, 12, 5, 6, 7, 8, 13, 14, 15, 16, 5, 7, 13, 15, 6, 8, 14, 16]

z = 15

for i in range(len(group_code)):
	if i == 16:
		z = 2
	grp = Group(
		grp_code = group_code[i],
		grp_name = group_name[i],
		grp_start_date = group_start[i],
		grp_end_date = group_end[i]
		)
	grp.save()
	if i == 3:
		m = Module.objects.get(id = 5)
		grp.grp_course.add(m)
	if i == 4:
		m = Module.objects.get(id = 1)
		grp.grp_course.add(m)
		m = Module.objects.get(id = 2)
		grp.grp_course.add(m)
	if i == 7:
		m = Module.objects.get(id = 3)
		grp.grp_course.add(m)
		m = Module.objects.get(id = 4)
		grp.grp_course.add(m)
	if i == 11:
		m = Module.objects.get(id = 6)
		grp.grp_course.add(m)
		m = Module.objects.get(id = 7)
		grp.grp_course.add(m)
	if i == 14:
		m = Module.objects.get(id = 10)
		grp.grp_course.add(m)
		m = Module.objects.get(id = 11)
		grp.grp_course.add(m)
	if i == 23:
		m = Module.objects.get(id = 8)
		grp.grp_course.add(m)
	if i == 24:
		m = Module.objects.get(id = 9)
		grp.grp_course.add(m)

# INSERT INTO RV1_group_grp_user (group_id, user_id) VALUES
# (1, 1),
# (1, 2),
# (1, 3),
# (1, 4),
# (1, 5),
# (1, 6),
# (1, 7),
# (1, 8),
# (1, 9),
# (1, 10),
# (1, 11),
# (1, 12),
# (1, 13),
# (1, 14),
# (1, 15),
# (1, 16),
# (2, 1),
# (2, 2),
# (2, 3),
# (2, 4),
# (2, 5),
# (2, 6),
# (2, 7),
# (2, 8),
# (2, 9),
# (2, 10),
# (2, 11),
# (2, 12),
# (2, 13),
# (2, 14),
# (2, 15),
# (2, 16),
# (2, 17),
# (3, 19),
# (3, 20),
# (3, 21),
# (3, 22),
# (3, 23),
# (3, 24),
# (4, 1),
# (4, 2),
# (4, 3),
# (4, 4),
# (4, 9),
# (4, 10),
# (4, 11),
# (4, 12),
# (5, 1),
# (5, 2),
# (5, 3),
# (5, 4),
# (6, 1),
# (6, 2),
# (7, 3),
# (7, 4),
# (8, 9),
# (8, 10),
# (8, 11),
# (8, 12),
# (9, 9),
# (9, 10),
# (10, 11),
# (10, 12),
# (11, 5),
# (11, 6),
# (11, 7),
# (11, 8),
# (11, 13),
# (11, 14),
# (11, 15),
# (11, 16),
# (12, 5),
# (12, 6),
# (12, 7),
# (12, 8),
# (13, 5),
# (13, 6),
# (14, 7),
# (14, 8),
# (15, 13),
# (15, 14),
# (15, 15),
# (15, 16),
# (16, 13),
# (16, 14),
# (17, 15),
# (17, 16),
# (18, 1),
# (18, 2),
# (18, 3),
# (18, 4),
# (18, 5),
# (18, 6),
# (18, 7),
# (18, 8),
# (19, 9),
# (19, 10),
# (19, 11),
# (19, 12),
# (19, 13),
# (19, 14),
# (19, 15),
# (19, 16),
# (20, 1),
# (20, 2),
# (20, 3),
# (20, 4),
# (20, 9),
# (20, 10),
# (20, 11),
# (20, 12),
# (21, 1),
# (21, 3),
# (21, 9),
# (21, 11),
# (22, 2),
# (22, 4),
# (22, 10),
# (22, 12),
# (23, 5),
# (23, 6),
# (23, 7),
# (23, 8),
# (23, 13),
# (23, 14),
# (23, 15),
# (23, 16),
# (24, 5),
# (24, 7),
# (24, 13),
# (24, 15),
# (25, 6),
# (25, 8),
# (25, 14),
# (25, 16),
# (26, 1),
# (26, 2),
# (26, 3),
# (26, 4),
# (26, 5),
# (26, 6),
# (26, 7),
# (26, 8),
# (26, 9),
# (26, 10),
# (26, 11),
# (26, 12),
# (26, 13),
# (26, 14),
# (26, 15),
# (26, 16),
# (26, 18),
# (27, 19),
# (27, 20),
# (27, 21),
# (27, 22),
# (27, 23),
# (27, 24),
# (28, 1),
# (28, 2),
# (28, 3),
# (28, 4),
# (28, 9),
# (28, 10),
# (28, 11),
# (28, 12),
# (29, 1),
# (29, 2),
# (29, 3),
# (29, 4),
# (30, 1),
# (30, 2),
# (31, 3),
# (31, 4),
# (32, 9),
# (32, 10),
# (32, 11),
# (32, 12),
# (33, 9),
# (33, 10),
# (34, 11),
# (34, 12),
# (35, 5),
# (35, 6),
# (35, 7),
# (35, 8),
# (35, 13),
# (35, 14),
# (35, 15),
# (35, 16),
# (36, 5),
# (36, 6),
# (36, 7),
# (36, 8),
# (37, 5),
# (37, 6),
# (38, 7),
# (38, 8),
# (39, 13),
# (39, 14),
# (39, 15),
# (39, 16),
# (40, 13),
# (40, 14),
# (41, 15),
# (41, 16),
# (42, 1),
# (42, 2),
# (42, 3),
# (42, 4),
# (42, 5),
# (42, 6),
# (42, 7),
# (42, 8),
# (43, 9),
# (43, 10),
# (43, 11),
# (43, 12),
# (43, 13),
# (43, 14),
# (43, 15),
# (43, 16),
# (44, 1),
# (44, 2),
# (44, 3),
# (44, 4),
# (44, 9),
# (44, 10),
# (44, 11),
# (44, 12),
# (45, 1),
# (45, 3),
# (45, 9),
# (45, 11),
# (46, 2),
# (46, 4),
# (46, 10),
# (46, 12),
# (47, 5),
# (47, 6),
# (47, 7),
# (47, 8),
# (47, 13),
# (47, 14),
# (47, 15),
# (47, 16),
# (48, 5),
# (48, 7),
# (48, 13),
# (48, 15),
# (49, 6),
# (49, 8),
# (49, 14),
# (49, 16)