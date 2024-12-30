import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from scipy.interpolate import interp1d
import numpy as np


# 模拟的物种分布地点经纬度数据（示例数据，可替换）
latitudes = np.array([30.0, 32.0, 35.0, 31.0, 33.0])  # 纬度数据
longitudes = np.array([120.0, 122.0, 121.0, 123.0, 124.0])  # 经度数据

# 创建地图对象，使用PlateCarree投影（经度 - 纬度坐标系统，常用且直观）
ax = plt.axes(projection=ccrs.PlateCarree())

# 设置地图范围（可根据实际数据范围合理调整）
ax.set_extent([min(longitudes) - 2, max(longitudes) + 2, min(latitudes) - 2, max(latitudes) + 2], crs=ccrs.PlateCarree())

# 绘制点
ax.scatter(longitudes, latitudes, marker='o', color='r', s=50, label='Distribution Points', transform=ccrs.PlateCarree())

# 添加地图特征，如海岸线、国界等，使地图更丰富直观
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)

# 计算经纬度对应的点坐标的凸包，用于生成分布范围界限
points = np.column_stack((longitudes, latitudes))
hull = ConvexHull(points)

# 获取凸包顶点
hull_points = points[hull.vertices]

# 计算凸包的几何中心
center = np.mean(hull_points, axis = 0)

# 缩放因子，可调节曲线范围
scale_factor = 1.2

# 对凸包顶点进行缩放
scaled_points = (hull_points - center) * scale_factor + center

# 获取缩放后的凸包顶点的经纬度
hull_lons = scaled_points[:, 0]
hull_lats = scaled_points[:, 1]
# 为了闭合曲线，添加起点到末尾
hull_lons = np.append(hull_lons, hull_lons[0])
hull_lats = np.append(hull_lats, hull_lats[0])

# 进行插值，使曲线平滑
num_interp_points = 100  # 插值点数量，可以调整
t = np.arange(len(hull_lons))
t_interp = np.linspace(0, len(hull_lons) - 1, num_interp_points)
interp_lons = interp1d(t, hull_lons, kind='cubic')(t_interp)
interp_lats = interp1d(t, hull_lats, kind='cubic')(t_interp)

# 绘制平滑曲线
ax.plot(interp_lons, interp_lats, 'b-', label='Smooth Distribution Boundary', transform=ccrs.PlateCarree())

# 填充凸包区域
ax.fill(interp_lons, interp_lats, color='b', alpha=0.3, transform=ccrs.PlateCarree())

# 添加图例，方便区分标记点和范围界限
ax.legend(loc='upper right')

# 设置标题
ax.set_title('Species Distribution Map')

# 显示地图
plt.show()