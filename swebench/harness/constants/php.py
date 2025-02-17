# Constants - Task Instance Installation Environment
SPECS_PHPSPREADSHEET = {
    "4313": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Writer/Ods/IndentTest.php"
        ],
    },
    "4214": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Calculation/Functions/MathTrig/RoundDownTest.php"
        ],
    },
    "4186": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Writer/Xlsx/FunctionPrefixTest.php"
        ],
    },
    "4114": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Worksheet/Issue4112Test.php"
        ],
    },
    "3940": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Worksheet/WorksheetTest.php"
        ],
    },
    "3903": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Shared/StringHelperTest.php"
        ],
    },
    "3570": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Calculation/Functions/LookupRef/VLookupTest.php"
        ],
    },
    "3463": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Writer/Xlsx/FunctionPrefixTest.php"
        ],
    },
    "3469": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Style/StyleTest.php"
        ],
    },
    "3659": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "./vendor/bin/phpunit --testdox --colors=never tests/PhpSpreadsheetTests/Worksheet/Table/Issue3635Test.php"
        ],
    },
}

SPECS_LARAVEL_FRAMEWORK = {
    "53914": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Integration/Database/DatabaseConnectionsTest.php"
        ],
    },
    "53206": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Support/SupportJsTest.php"
        ],
    },
    "52866": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Container/ContextualAttributeBindingTest.php"
        ],
    },
    "52684": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Support/SupportStrTest.php"
        ],
    },
    "52680": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Database/DatabaseEloquentInverseRelationTest.php"
        ],
    },
    "52451": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Validation/ValidationValidatorTest.php --filter 'custom'"
        ],
    },
    "53949": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Support/OnceTest.php"
        ],
    },
    "51890": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Validation/ValidationValidatorTest.php --filter 'attribute'"
        ],
    },
    "51195": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/View/Blade/BladeVerbatimTest.php"
        ],
    },
    "48636": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Database/DatabaseEloquentModelTest.php"
        ],
    },
    "48573": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Cache/CacheArrayStoreTest.php"
        ],
    },
    "46234": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Routing/RoutingUrlGeneratorTest.php"
        ],
    },
    "53696": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Database/DatabaseSchemaBlueprintTest.php"
        ],
    },
}

SPECS_PHP_CS_FIXER = {
    "8367": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/Import/FullyQualifiedStrictTypesFixerTest.php"
        ],
    },
    "8331": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/LanguageConstruct/NullableTypeDeclarationFixerTest.php"
        ],
    },
    "8075": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/PhpUnit/PhpUnitAttributesFixerTest.php"
        ],
    },
    "8064": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/StringNotation/SimpleToComplexStringVariableFixerTest.php"
        ],
    },
    "7998": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/Casing/ConstantCaseFixerTest.php",
        ],
    },
    "7875": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/Whitespace/StatementIndentationFixerTest.php",
        ],
    },
    "7635": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/Import/FullyQualifiedStrictTypesFixerTest.php",
        ],
    },
    "7523": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/Operator/BinaryOperatorSpacesFixerTest.php",
        ],
    },
    "8256": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/PhpTag/BlankLineAfterOpeningTagFixerTest.php",
        ],
    },
    "7663": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Fixer/Whitespace/StatementIndentationFixerTest.php",
        ],
    },
}

SPECS_CARBON = {
    "3103": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonImmutable/SettersTest.php"
        ],
    },
    "3098": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonInterval/ConstructTest.php"
        ],
    },
    "3073": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonInterval/TotalTest.php"
        ],
    },
    "3041": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonPeriod/CreateTest.php"
        ],
    },
    "3005": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonInterval/ConstructTest.php"
        ],
    },
    "2981": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonInterval/TotalTest.php"
        ],
    },
    "2813": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        # Patch involves adding a new dependency, so we need to re-install
        "build": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Factory/FactoryTest.php"
        ],
    },
    "2752": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonImmutable/IsTest.php"
        ],
    },
    "2665": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/Carbon/RoundTest.php"
        ],
    },
    "2762": {
        "base_docker_specs": {"php_version": "8.3.16"},
        "docker_specs": {"php_version": "8.3.16"},
        "install": ["composer update", "composer install"],
        "test_cmd": [
            "vendor/bin/phpunit --testdox --colors=never tests/CarbonInterval/RoundingTest.php"
        ],
    },
}

MAP_REPO_VERSION_TO_SPECS_PHP = {
    "phpoffice/phpspreadsheet": SPECS_PHPSPREADSHEET,
    "laravel/framework": SPECS_LARAVEL_FRAMEWORK,
    "php-cs-fixer/php-cs-fixer": SPECS_PHP_CS_FIXER,
    "briannesbitt/carbon": SPECS_CARBON,
}

# Constants - Repository Specific Installation Instructions
MAP_REPO_TO_INSTALL_PHP = {}
