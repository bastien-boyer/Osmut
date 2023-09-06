import unittest

if __name__ == "__main__":
    # Découvrez et chargez automatiquement tous les tests
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="*.py")

    # Exécutez les tests
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    # Vous pouvez également obtenir des statistiques sur les tests exécutés
    print("Nombre de tests exécutés :", result.testsRun)
    print("Erreurs :", len(result.errors))
    print("Échecs :", len(result.failures))
