# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class spider(object):

    def get_geetest_image(self, name, flag):
        """
        获得验证码图片
        """
        bottom, top, left, right = self.get_position(flag)
        print("验证图片位置", bottom, top, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, bottom, right, top))
        captcha.save(name)
        return captcha

    def get_position(self, flag):

        """
        获取验证码图片位置
        """
        img = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "canvas.geetest_canvas_slice")))
        time.sleep(2)
        if flag:
            # 执行js获取不带缺口的原图
            self.browser.execute_script(
                'document.getElementsByClassName("geetest_canvas_fullbg")[0].setAttribute("style", "")')
        else:
            # 执行js,把缺口复原
            self.browser.execute_script(
                'document.getElementsByClassName("geetest_canvas_fullbg")[0].setAttribute("style", "opacity: 1; display: none;")')
        location = img.location
        print("图片坐标为：{}".format(location))
        size = img.size
        print("图片大小为：{}".format(size))
        bottom, top, left, right = location["y"], location["y"] + size["height"], location["x"], location["x"] + size[
            "width"]

        return (bottom, top, left, right)

    def get_gap(self, image1, image2):

        """
        获取缺口位置，通过比较像素值
        """
        for i in range(LEFT, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    return i
        return LEFT

    def is_pixel_equal(self, image1, image2, x, y):

        """
        像素值比较，若三个通道均为出现超过阈值的变化，返回True
        """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        if abs(pixel1[0] - pixel2[0]) < THRESHOLD and abs(pixel1[1] - pixel2[1]) < THRESHOLD and abs(
                pixel1[2] - pixel2[2]) < THRESHOLD:
            return True
        else:
            return False

    def get_slider(self):

        """
        获取滑块
        """
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "geetest_slider_button")))

    def get_track(self, distance):

        """
        获取滑块移动轨迹的列表,distance是缺口的左侧横坐标值
        """
        track = []
        current = 0
        mid = distance * 0.8
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 2.5
            else:
                a = -3.5
            v0 = v
            v = v0 + a * t
            move = v0 * t + 0.5 * a * t * t
            current += move
            track.append(round(move))
        return track
