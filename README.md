Pentru a folosi proiectul este necesar sa instalati librariile necesare .Acestea se instaleaza din terminal folosind comanda : pip install -r 
Pentru a rula puteti folosi comanda behave -f html -o numeRaport.html -- tags=numeTest .
Numele tag-ului se poate gasi deasupra scenariului pe care vreti sa il testati , de exemplu :@test4 .


LIMBAJ :
Am ales să efectuez testarea folosind limbajul de programare Python și IDE-ul PyCharm. Pentru a automatiza interacțiunea cu site-ul JulesApp, am folosit bibliotecile Selenium, webdriver-manager, behave și behave-html-formatter. Aceste biblioteci pot fi instalate din secțiunea "Pachete Python" din PyCharm. Acolo, am introdus numele fiecărei biblioteci în câmpul de căutare și am apăsat butonul "Instalare" pentru a le adăuga în proiect.
IMPORTANTA TESTARE AUTOMATA :
estarea automată permite executarea rapidă și repetabilă a testelor și poate fi integrată în fluxul de dezvoltare continuă. Testele automate pot fi reutilizate pentru versiunile viitoare ale software-ului. Acest proces asigură o calitate constantă a produsului și reduce riscul de introducere a defectelor în noile versiuni.


STRUCTURA :
Folderele principale sunt urmatoarele :
  Features – care continue fisiere scrise in limbajul gherkin , unde se vor  descrie scenariile .
  Pages -  pagini de mapare pentru fiecare element din browser
  Steps – maparea tehnica a fisierelor de business     

  
LIBRARI NECESARE :
In acest proiect am folosit 4 librarii principale : selenium , behave , behave-html-formatter , webdriver-manager 
    Acestea pot fi instalate direct din terminal folosit comanda  : pip install nume_librarie .
