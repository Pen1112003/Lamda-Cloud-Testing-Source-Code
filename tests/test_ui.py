import pytest
import os
import platform

# Skip all tests if selenium is not installed
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

BASE_URL = os.getenv('APP_URL', 'https://lamda-cloud-tes.uc.r.appspot.com')

@pytest.fixture
def driver():
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
        
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    try:
        # Check if running on M1/M2 Mac
        if platform.processor() == 'arm':
            chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            service = Service()
        else:
            service = Service(ChromeDriverManager().install())
            
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    except Exception as e:
        pytest.skip(f"Failed to initialize Chrome driver: {str(e)}")

@pytest.mark.ui
def test_home_page(driver):
    """Test home page UI elements"""
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
        
    driver.get(f"{BASE_URL}/")
    assert "Smartphone X" in driver.page_source
    assert driver.find_element(By.TAG_NAME, "h1").text == "Welcome to Our Store"

@pytest.mark.ui
def test_products_page(driver):
    """Test products page UI elements"""
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
        
    driver.get(f"{BASE_URL}/products")
    products = driver.find_elements(By.CLASS_NAME, "product")
    assert len(products) > 0
    assert "Laptop Pro" in driver.page_source

@pytest.mark.ui
def test_product_detail(driver):
    """Test product detail page UI elements"""
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
        
    driver.get(f"{BASE_URL}/product/1")
    assert "Smartphone X" in driver.page_source
    assert driver.find_element(By.CLASS_NAME, "product-detail")

@pytest.mark.ui
def test_category_page(driver):
    """Test category page UI elements"""
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
        
    driver.get(f"{BASE_URL}/category/1")
    assert "Electronics" in driver.page_source
    products = driver.find_elements(By.CLASS_NAME, "product")
    assert len(products) > 0

@pytest.mark.ui
def test_navigation(driver):
    """Test navigation between pages"""
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium is not installed")
        
    # Start at home page
    driver.get(f"{BASE_URL}/")
    
    # Click products link
    products_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Products"))
    )
    products_link.click()
    assert "products" in driver.current_url
    
    # Click first product
    product_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product"))
    )
    product_link.click()
    assert "product" in driver.current_url 