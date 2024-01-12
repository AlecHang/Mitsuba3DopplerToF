
import sys, os
module_path = 'C:\\Users\\Admin\\projects\\test\\Mitsuba3DopplerToF\\build\\Debug\\python'
sys.path.append(module_path)
import mitsuba as mi
import matplotlib.pyplot as plt

#.cmake-build-debug-mingw.Debug.python
mi.set_variant('cuda_ad_rgb')
print(os.getpid())
print(mi.variants())

scene =  mi.load_file("C:\\Users\\Admin\\projects\\test\\Mitsuba3DopplerToF\\configs_example\\scene.xml", parallel=False)
'''
params = mi.traverse(scene)

params['PerspectiveCamera.film.size'] = [640, 320]
params['PerspectiveCamera.shutter_open_time'] = 0.0015
params['Instance.to_world'] = mi.Transform4f([[-0.780869, -0.0486324, -0.622799, 0],
                                              [0, 0.996965, -0.0778499, 0.5],
                                              [0.624695, -0.0607905, -0.778499, 0],
                                              [0, 0, 0, 1]])
params.update()
'''
image = mi.render(scene, spp=512)

#mi.Bitmap(image).write('dining-room.exr')
mi.util.write_bitmap('frame_00.png', mi.Bitmap(image))

plt.axis("off")
plt.imshow(image ** (1.0 / 2.2)); # approximate sRGB tonemapping
plt.show()