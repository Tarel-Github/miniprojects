using MahApps.Metro.Controls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Diagnostics;
using SmartHomeMonitoringApp.Views;

namespace SmartHomeMonitoringApp
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void MetroWindow_Loaded(object sender, RoutedEventArgs e)
        {
            // <Frame> ==> Page.xaml
            // <ContentControl> ==> UserControl.xaml
            // ActiveItem.Content = new Views.DataBaseControl();
        }

        private void MnuExitSubsribe_Click(object sender, RoutedEventArgs e)
        {
            Process.GetCurrentProcess().Kill();  // 작업관리자에서 프로세스 종료! 이게 더 빠름
            //Environment.Exit(0);    // 끝내기      // 0이 일반종료, 이외에도 코드가 많음, 종료 속도가 조금 느림
        }

        // MQTT 시작메뉴 클릭이벤트 핸들러
        private void MnuStartSubsribe_Click(object sender, RoutedEventArgs e)
        {
            var mqttPopWin = new MqttPopupWindow();
            mqttPopWin.Owner = this;
            mqttPopWin.WindowStartupLocation = WindowStartupLocation.CenterOwner;
            var result = mqttPopWin.ShowDialog();

            if(result == true)
            {
                ActiveItem.Content = new Views.DataBaseControl();
            }
        }
    }
}
