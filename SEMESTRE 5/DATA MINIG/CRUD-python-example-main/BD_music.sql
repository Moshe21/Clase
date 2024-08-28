create database My_server;
use My_server;

CREATE TABLE artistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    pais VARCHAR(50),
    fecha_nacimiento DATE,
    descripcion TEXT
);
-- Crear la tabla "genero"
CREATE TABLE genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);
-- Insertar registros de ejemplo en la tabla "artistas"
INSERT INTO artistas (nombre, pais, fecha_nacimiento, descripcion)
VALUES
    ('Artista1', 'País1', '1990-05-15', 'Descripción del artista 1'),
    ('Artista2', 'País2', '1985-12-03', 'Descripción del artista 2'),
    ('Artista3', 'País3', '2000-08-20', 'Descripción del artista 3');
-- Insertar registros de ejemplo en la tabla "genero"
INSERT INTO genero (nombre, descripcion)
VALUES
    ('Rock', 'Descripción del género Rock'),
    ('Pop', 'Descripción del género Pop'),
    ('Jazz', 'Descripción del género Jazz');
    
INSERT INTO artistas (nombre, pais, fecha_nacimiento, descripcion) VALUES
('Luis Miguel', 'México', '1970-04-19', 'Cantante conocido como "El Sol de México", con una carrera de más de 40 años.'),
('Shakira', 'Colombia', '1977-02-02', 'Cantante, compositora y productora discográfica, conocida por su estilo único y su fusión de géneros.'),
('Freddie Mercury', 'Reino Unido', '1946-09-05', 'Vocalista de la banda Queen, reconocido por su poderosa voz y carisma.'),
('Beyoncé', 'Estados Unidos', '1981-09-04', 'Cantante, actriz y empresaria, conocida por su potente voz y presencia escénica.'),
('Michael Jackson', 'Estados Unidos', '1958-08-29', 'El Rey del Pop, conocido por su música innovadora y su habilidad para el baile.'),
('Selena Quintanilla', 'Estados Unidos', '1971-04-16', 'Cantante de música tejana, considerada la Reina del Tex-Mex.'),
('David Bowie', 'Reino Unido', '1947-01-08', 'Cantante, compositor y actor, conocido por su influencia en la música pop y rock.'),
('Adele', 'Reino Unido', '1988-05-05', 'Cantante y compositora británica, conocida por su poderosa voz y baladas emocionales.'),
('Elvis Presley', 'Estados Unidos', '1935-01-08', 'El Rey del Rock and Roll, famoso por su estilo único y revolucionario en la música.'),
('Madonna', 'Estados Unidos', '1958-08-16', 'Cantante, actriz y empresaria, conocida como la Reina del Pop.'),
('Carlos Vives', 'Colombia', '1961-08-07', 'Cantante, compositor y actor, conocido por revitalizar la música vallenato.'),
('Juan Gabriel', 'México', '1950-01-07', 'Cantante, compositor y actor, conocido por su contribución a la música popular mexicana.'),
('Whitney Houston', 'Estados Unidos', '1963-08-09', 'Cantante y actriz, reconocida por su voz poderosa y su influencia en la música pop y R&B.'),
('Bob Marley', 'Jamaica', '1945-02-06', 'Cantante, compositor y guitarrista, conocido por popularizar la música reggae en todo el mundo.'),
('Celia Cruz', 'Cuba', '1925-10-21', 'La Reina de la Salsa, conocida por su energía en el escenario y su influencia en la música latina.'),
('Paul McCartney', 'Reino Unido', '1942-06-18', 'Cantante, compositor y bajista, conocido por su trabajo con The Beatles y su exitosa carrera solista.'),
('Rihanna', 'Barbados', '1988-02-20', 'Cantante, actriz y empresaria, conocida por su estilo versátil y éxitos en múltiples géneros musicales.'),
('Prince', 'Estados Unidos', '1958-06-07', 'Cantante, compositor y productor, conocido por su estilo innovador y su habilidad para mezclar géneros.'),
('Taylor Swift', 'Estados Unidos', '1989-12-13', 'Cantante y compositora, conocida por su habilidad para escribir letras sinceras y emocionalmente resonantes.'),
('Enrique Iglesias', 'España', '1975-05-08', 'Cantante y compositor, conocido por su contribución a la música pop y latina.'),
('J Balvin', 'Colombia', '1985-05-07', 'Cantante de reguetón, conocido por ser uno de los exponentes más populares de este género a nivel mundial.'),
('Kurt Cobain', 'Estados Unidos', '1967-02-20', 'Cantante y guitarrista, conocido por ser el líder de la banda Nirvana y su influencia en el grunge.'),
('Lady Gaga', 'Estados Unidos', '1986-03-28', 'Cantante, actriz y productora, conocida por su estilo excéntrico y su poderosa voz.'),
('Andrea Bocelli', 'Italia', '1958-09-22', 'Tenor, compositor y productor musical, conocido por su voz excepcional y su habilidad en la ópera.'),
('Bad Bunny', 'Puerto Rico', '1994-03-10', 'Cantante de trap y reguetón, conocido por su estilo único y su impacto en la música latina.'),
('John Lennon', 'Reino Unido', '1940-10-09', 'Cantante y compositor, conocido por su trabajo con The Beatles y su carrera como solista.'),
('Ed Sheeran', 'Reino Unido', '1991-02-17', 'Cantante y compositor, conocido por sus baladas acústicas y su habilidad para contar historias a través de la música.'),
('Bruno Mars', 'Estados Unidos', '1985-10-08', 'Cantante, compositor y productor, conocido por su versatilidad y habilidad para mezclar géneros musicales.'),
('Ariana Grande', 'Estados Unidos', '1993-06-26', 'Cantante y actriz, conocida por su poderosa voz y su éxito en el pop contemporáneo.'),
('Elton John', 'Reino Unido', '1947-03-25', 'Cantante, compositor y pianista, conocido por su larga carrera y su influencia en la música pop y rock.'),
('Billie Eilish', 'Estados Unidos', '2001-12-18', 'Cantante y compositora, conocida por su estilo único y su éxito en la música pop contemporánea.'),
('Frank Sinatra', 'Estados Unidos', '1915-12-12', 'Cantante y actor, conocido por su voz inconfundible y su influencia en la música popular.'),
('Gloria Estefan', 'Cuba', '1957-09-01', 'Cantante y compositora, conocida por su influencia en la música latina y pop.'),
('Plácido Domingo', 'España', '1941-01-21', 'Tenor y director de orquesta, conocido por su poderosa voz y su habilidad en la ópera.'),
('Justin Bieber', 'Canadá', '1994-03-01', 'Cantante y compositor, conocido por su éxito desde una edad temprana y su influencia en el pop contemporáneo.'),
('Shawn Mendes', 'Canadá', '1998-08-08', 'Cantante y compositor, conocido por su estilo pop y sus baladas románticas.'),
('Thalía', 'México', '1971-08-26', 'Cantante y actriz, conocida por su influencia en la música pop latina y su éxito en telenovelas.'),
('Marvin Gaye', 'Estados Unidos', '1939-04-02', 'Cantante y compositor, conocido por su influencia en el soul y el R&B.'),
('Alejandro Sanz', 'España', '1968-12-18', 'Cantante y compositor, conocido por su habilidad para mezclar géneros y su influencia en la música pop latina.'),
('Jennifer Lopez', 'Estados Unidos', '1969-07-24', 'Cantante, actriz y empresaria, conocida por su influencia en la música pop y latina.'),
('Stevie Wonder', 'Estados Unidos', '1950-05-13', 'Cantante, compositor y multiinstrumentista, conocido por su influencia en el soul, R&B y pop.'),
('Mick Jagger', 'Reino Unido', '1943-07-26', 'Cantante y compositor, conocido por ser el vocalista de The Rolling Stones y su influencia en el rock.'),
('Amy Winehouse', 'Reino Unido', '1983-09-14', 'Cantante y compositora, conocida por su voz única y su influencia en el soul y jazz contemporáneo.'),
('Luis Fonsi', 'Puerto Rico', '1978-04-15', 'Cantante y compositor, conocido por su éxito en la música pop latina y reguetón.'),
('Janis Joplin', 'Estados Unidos', '1943-01-19', 'Cantante, conocida por su voz única y su influencia en el rock y blues.'),
('Vicente Fernández', 'México', '1940-02-17', 'Cantante y actor, conocido como el "Rey de la Música Ranchera".'),
('Dua Lipa', 'Reino Unido', '1995-08-22', 'Cantante y compositora, conocida por su estilo pop y su influencia en la música contemporánea.'),
('Bruce Springsteen', 'Estados Unidos', '1949-09-23', 'Cantante y compositor, conocido por su estilo rock y sus letras emotivas.'),
('Charlie Puth', 'Estados Unidos', '1991-12-02', 'Cantante, compositor y productor, conocido por su habilidad para mezclar géneros y su éxito en la música pop.'),
('Sam Smith', 'Reino Unido', '1992-05-19', 'Cantante y compositor, conocido por su estilo pop y soul y su voz distintiva.'),
('Christina Aguilera', 'Estados Unidos', '1980-12-18', 'Cantante y actriz, conocida por su poderosa voz y su influencia en la música pop y R&B.');


INSERT INTO genero (nombre, descripcion) VALUES
('Pop', 'Un género musical popular que combina elementos de otros géneros como el rock, el dance y la música urbana. Es conocido por su enfoque en la melodía y el atractivo comercial. Artistas como Michael Jackson y Madonna han sido íconos del pop.'),
('Rock', 'Género musical que se originó en la década de 1950, caracterizado por el uso de guitarras eléctricas, un ritmo fuerte y letras a menudo rebeldes. Artistas como The Beatles y Queen han sido fundamentales en su desarrollo.'),
('Reguetón', 'Un género musical de origen latino, caracterizado por su ritmo urbano y letras que a menudo abordan temas de fiesta, amor y vida urbana. J Balvin y Bad Bunny son algunos de los artistas más influyentes en este género.'),
('Soul', 'Género musical que surgió en los Estados Unidos en la década de 1950, conocido por sus vocales emotivos y su influencia del gospel. Marvin Gaye y Stevie Wonder son íconos de este género.'),
('R&B', 'Género musical que combina elementos del soul, el funk, el pop y el hip hop. Es conocido por sus ritmos suaves y letras románticas. Artistas como Whitney Houston y Rihanna han sido influyentes en este género.'),
('Vallenato', 'Género musical de origen colombiano, conocido por su uso de acordeones y letras que narran historias de la vida cotidiana. Carlos Vives es uno de los artistas más reconocidos en este género.'),
('Ópera', 'Un género musical clásico caracterizado por la combinación de música orquestal y canto, con un enfoque en la expresividad vocal. Andrea Bocelli y Plácido Domingo son tenores famosos en este género.'),
('Trap', 'Género de música urbana que surgió en el sur de los Estados Unidos, caracterizado por sus ritmos pesados y letras crudas. Bad Bunny ha sido un pionero en llevar este género a la música latina.'),
('Grunge', 'Subgénero del rock que surgió en Seattle en la década de 1990, conocido por su sonido crudo y letras introspectivas. Kurt Cobain, como líder de Nirvana, es una figura icónica de este género.'),
('Salsa', 'Género musical latino que combina elementos del jazz, el son cubano y otros ritmos afrolatinos. Celia Cruz, conocida como la Reina de la Salsa, es una de las figuras más importantes del género.'),
('Reggae', 'Género musical originario de Jamaica, conocido por su ritmo relajado y letras que a menudo tratan temas sociales y políticos. Bob Marley es la figura más reconocida del reggae a nivel mundial.'),
('Jazz', 'Género musical que se originó en la comunidad afroamericana a principios del siglo XX, conocido por su improvisación y complejidad armónica. Amy Winehouse incorporó elementos de jazz en su música.'),
('Tejano', 'Género musical popular en Texas y México, que combina elementos de la música mexicana, polka y otros estilos. Selena Quintanilla fue una de las artistas más influyentes en este género.'),
('Country', 'Género musical originario del sur de los Estados Unidos, conocido por su enfoque en instrumentos como la guitarra, el banjo y la armónica, y letras sobre la vida rural. Taylor Swift comenzó su carrera en este género.'),
('Funk', 'Género musical que se originó en la década de 1960, caracterizado por su ritmo contagioso y su énfasis en el bajo. Prince es conocido por su capacidad para mezclar funk con otros géneros.'),
('Rock and Roll', 'Subgénero del rock que surgió en la década de 1950, caracterizado por su ritmo rápido y su enfoque en la guitarra eléctrica. Elvis Presley, conocido como el Rey del Rock and Roll, fue un pionero en este género.'),
('Pop Latino', 'Un subgénero del pop que incorpora elementos de la música latina. Thalía y Enrique Iglesias son dos de los artistas más influyentes en este género.'),
('Blues', 'Género musical originario del sur de los Estados Unidos, conocido por su estructura de acordes simple y sus letras melancólicas. Janis Joplin es una de las voces más reconocidas del blues.'),
('Ranchera', 'Género musical tradicional mexicano, conocido por su melodía emotiva y letras que hablan de amor, desamor y el orgullo mexicano. Vicente Fernández es uno de los máximos exponentes de la música ranchera.'),
('Dance', 'Género de música electrónica diseñado para ser bailado, que incluye subgéneros como el house, techno y trance. Artistas pop como Madonna han incorporado elementos de dance en su música.'),
('Balada', 'Un estilo de música que se centra en canciones de amor y letras emocionales, a menudo con un acompañamiento suave. Artistas como Luis Miguel y Adele son conocidos por sus baladas poderosas.'),
('Electropop', 'Un subgénero del pop que incorpora elementos de la música electrónica. Dua Lipa ha llevado este género a la popularidad con su estilo moderno.'),
('Disco', 'Género musical que se popularizó en la década de 1970, caracterizado por su ritmo bailable y su estilo festivo. Aunque no se menciona directamente, influencias de este género pueden verse en la música de artistas como Michael Jackson.'),
('Tropical', 'Un género amplio que incluye estilos como la salsa, cumbia, y merengue, entre otros. Gloria Estefan ha sido una de las principales figuras en popularizar la música tropical.'),
('Hip Hop', 'Género musical que surgió en los años 70 en Nueva York, caracterizado por el rap y la producción de beats. Aunque no se menciona directamente en la tabla anterior, influencias de hip hop pueden verse en la música de artistas como Rihanna.'),
('Música Clásica', 'Género musical que abarca una amplia gama de estilos que datan desde la Edad Media hasta el presente. Andrea Bocelli ha trabajado con repertorio clásico en su carrera.'),
('Merengue', 'Género musical bailable originario de la República Dominicana, conocido por su ritmo rápido y su uso de instrumentos como la güira y el acordeón. Aunque no se menciona directamente, influencias de merengue pueden verse en la música de artistas tropicales.'),
('Rock Latino', 'Subgénero del rock que incorpora elementos de la música latina. Juan Gabriel y otros artistas mexicanos han fusionado elementos de rock con estilos latinos.'),
('Bolero', 'Género musical de origen cubano conocido por su ritmo lento y letras románticas. Luis Miguel es conocido por interpretar boleros a lo largo de su carrera.'),
('Opera Pop', 'Una fusión de la música clásica con el pop, que busca hacer la ópera más accesible al público general. Andrea Bocelli es un pionero en este género.'),
('Heavy Metal', 'Subgénero del rock caracterizado por su sonido pesado y el uso de guitarras distorsionadas. Aunque no se menciona directamente, el heavy metal ha influenciado a muchos géneros de rock.'),
('Música Regional Mexicana', 'Un término amplio que engloba varios géneros de música tradicional mexicana, incluyendo ranchera, norteño, y banda. Vicente Fernández es un ícono de la música regional mexicana.'),
('Indie Pop', 'Subgénero del pop que se caracteriza por su enfoque en la independencia creativa y la producción no convencional. Artistas como Billie Eilish han sido parte de la escena indie pop.'),
('Flamenco', 'Género musical y baile tradicional de España, caracterizado por su pasión y expresividad. Aunque no se menciona directamente, el flamenco ha influenciado a muchos artistas españoles.'),
('Punk Rock', 'Subgénero del rock conocido por su energía cruda, actitud rebelde y letras políticas. Aunque no se menciona directamente, el punk rock ha influido en muchos géneros de rock alternativo.'),
('Música Latina', 'Un término general que engloba diversos géneros musicales de América Latina, desde el reguetón hasta la salsa. Shakira y Ricky Martin son dos de los artistas más influyentes en este género.'),
('Jazz Latino', 'Una fusión del jazz con ritmos latinos como la salsa, el son cubano y la bossa nova. Artistas como Celia Cruz han influenciado el desarrollo del jazz latino.'),
('Fado', 'Género musical tradicional portugués caracterizado por su tono melancólico y letras que hablan de la saudade (nostalgia). Aunque no se menciona directamente, es un género importante en la música de Portugal.'),
('New Wave', 'Subgénero del rock que surgió en la década de 1980, conocido por su uso de sintetizadores y su enfoque en la estética moderna. David Bowie experimentó con elementos de new wave en su música.'),
('Tango', 'Género musical y baile originario de Argentina, conocido por su pasión y melancolía. Aunque no se menciona directamente, es uno de los géneros más importantes de la música argentina.'),
('Cumbia', 'Género musical originario de Colombia, conocido por su ritmo bailable y su popularidad en toda América Latina. Aunque no se menciona directamente, es un género influyente en la música tropical.');

-- consultas--
select * from artistas where id <10;


